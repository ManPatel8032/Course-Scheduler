from django.http import JsonResponse
import subprocess
import json
import os

def generate_schedule(request):
    """
    This view runs the C++ scheduling algorithm and returns the generated course order as JSON.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    algo_dir = os.path.join(base_dir, "algorithms")

    # C++ executable path (scheduler.cpp → compiled to scheduler)
    cpp_executable = os.path.join(algo_dir, "scheduler")

    # Run the compiled C++ program
    subprocess.run([cpp_executable], cwd=algo_dir)

    # Read output JSON from C++ algorithm
    output_path = os.path.join(algo_dir, "output_order.json")
    with open(output_path, "r") as f:
        data = json.load(f)

    # Return JSON response to frontend or API caller
    return JsonResponse(data)
