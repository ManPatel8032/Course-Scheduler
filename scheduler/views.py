from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import subprocess
import json
import os
import shutil
import platform

def home(request):
    """
    Display the course catalog for students to browse and select courses.
    """
    # Load course catalog
    catalog_path = os.path.join(os.path.dirname(__file__), 'course_catalog.json')
    
    try:
        with open(catalog_path, 'r') as f:
            catalog = json.load(f)
    except FileNotFoundError:
        catalog = {"courses": []}
    
    # Group courses by department
    courses_by_department = {}
    for course in catalog.get('courses', []):
        dept = course.get('department', 'Other')
        if dept not in courses_by_department:
            courses_by_department[dept] = []
        courses_by_department[dept].append(course)
    
    # Convert catalog to JSON string for JavaScript
    import json as json_lib
    catalog_json = json_lib.dumps(catalog['courses'])
    
    return render(request, 'scheduler/home.html', {
        'catalog': catalog,
        'courses_by_department': courses_by_department,
        'catalog_json': catalog_json
    })

@csrf_exempt
def generate_schedule(request):
    """
    This view runs the C++ scheduling algorithm and returns the generated course order as JSON.
    
    GET: Uses default input_sample.json
    POST: Accepts custom course data in request body
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    algo_dir = os.path.join(base_dir, 'algorithms')
    input_path = os.path.join(algo_dir, 'input_courses.json')
    output_path = os.path.join(algo_dir, 'output_order.json')
    # Use .exe on Windows, otherwise plain name
    executable_name = 'scheduler.exe' if platform.system() == 'Windows' else 'scheduler'
    cpp_executable = os.path.join(algo_dir, executable_name)

    try:
        # Handle GET request - use default input file
        if request.method == "GET":
            # Copy default input to working input file
            default_input = os.path.join(algo_dir, 'input_sample.json')
            if not os.path.exists(default_input):
                return JsonResponse({"error": "Default input file not found"}, status=500)
            
            # Copy default input to input_courses.json
            shutil.copy2(default_input, input_path)
        
        # Handle POST request - use custom input
        elif request.method == "POST":
            try:
                data = json.loads(request.body)
                
                # Load the full course catalog to find prerequisite details
                catalog_path = os.path.join(os.path.dirname(__file__), 'course_catalog.json')
                with open(catalog_path, 'r') as f:
                    catalog = json.load(f)
                
                catalog_courses = {c["code"]: c for c in catalog.get("courses", [])}
                selected_codes = [c["code"] for c in data.get("courses", [])]
                
                # Build a set of all courses we need (selected + prerequisites)
                courses_needed = set(selected_codes)
                
                # Add all prerequisites recursively
                def add_prerequisites(code, visited=None):
                    if visited is None:
                        visited = set()
                    if code in visited:
                        return
                    visited.add(code)
                    
                    if code in catalog_courses:
                        for prereq in catalog_courses[code].get("prerequisites", []):
                            courses_needed.add(prereq)
                            add_prerequisites(prereq, visited)
                
                for code in selected_codes:
                    add_prerequisites(code)
                
                # Build simplified data with only needed courses
                simplified_data = {
                    "courses": [
                        {
                            "code": cat_course["code"], 
                            "prerequisites": cat_course.get("prerequisites", [])
                        } 
                        for code in courses_needed
                        if code in catalog_courses
                        for cat_course in [catalog_courses[code]]
                    ]
                }
                
                with open(input_path, "w") as f:
                    json.dump(simplified_data, f, indent=4)
            except json.JSONDecodeError:
                return JsonResponse({"error": "Invalid JSON in request body"}, status=400)
        
        # Ensure input file exists
        if not os.path.exists(input_path):
            return JsonResponse({"error": "Input file not found"}, status=500)
        
        # Check if C++ executable exists
        if not os.path.exists(cpp_executable):
            return JsonResponse({
                "error": "Scheduler executable not found. Please compile scheduler.cpp first"
            }, status=500)
        
        # Run the compiled C++ program
        result = subprocess.run([cpp_executable], cwd=algo_dir, capture_output=True, text=True)
        
        if result.returncode != 0:
            return JsonResponse({
                "error": "Scheduler failed",
                "details": result.stderr
            }, status=500)
        
        # Read and return the generated result
        if not os.path.exists(output_path):
            return JsonResponse({"error": "Output file not generated"}, status=500)
        
        with open(output_path, "r") as f:
            output = json.load(f)
        
        return JsonResponse(output)
    
    except Exception as e:
        return JsonResponse({"error": f"Internal error: {str(e)}"}, status=500)
