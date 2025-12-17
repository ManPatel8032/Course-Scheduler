# Course Scheduler

A sophisticated web application for intelligent course scheduling that optimizes student course sequences based on prerequisites using advanced algorithms. This full-stack project demonstrates expertise in backend development, algorithm design, and modern web technologies.

## 🚀 Features

- **Intelligent Scheduling Algorithm**: Custom C++ implementation using topological sorting to generate optimal course sequences
- **Interactive Web Interface**: Modern, responsive UI built with HTML5, CSS3, and vanilla JavaScript
- **Dynamic Course Selection**: Real-time course filtering and selection with visual feedback
- **Prerequisite Resolution**: Automatic inclusion of prerequisite courses in generated schedules
- **RESTful API**: Clean Django REST endpoints for schedule generation
- **Cross-Platform Compatibility**: Works on Windows, macOS, and Linux
- **Error Handling**: Comprehensive error handling with user-friendly messages

## 🛠️ Tech Stack

### Backend
- **Django** - Python web framework for robust backend architecture
- **C++** - High-performance scheduling algorithm implementation
- **JSON** - Data interchange format for course catalogs and schedules

### Frontend
- **HTML5** - Semantic markup and accessibility
- **CSS3** - Modern styling with responsive design
- **Vanilla JavaScript** - DOM manipulation and AJAX for dynamic interactions

### Development Tools
- **Git** - Version control
- **Virtual Environment** - Python dependency isolation
- **Subprocess Management** - Seamless integration between Python and C++

## 📋 Prerequisites

- Python 3.8+
- C++ Compiler (GCC/Clang on Unix, MSVC on Windows)
- Git

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ManPatel8032/course-scheduler.git
   cd course-scheduler
   ```

2. **Set up Python environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Compile the C++ algorithm**
   ```bash
   cd algorithms
   # On Windows
   g++ scheduler.cpp -o scheduler.exe -std=c++11
   
   # On Unix/Linux/macOS
   g++ scheduler.cpp -o scheduler -std=c++11
   cd ..
   ```

4. **Run database migrations** (if using Django models)
   ```bash
   python manage.py migrate
   ```

## 🚀 Usage

1. **Start the development server**
   ```bash
   python manage.py runserver
   ```

2. **Access the application**
   - Open your browser and navigate to `http://127.0.0.1:8000/`
   - Browse the course catalog
   - Select desired courses
   - Click "Generate Schedule" to see the optimized course sequence

## 📁 Project Structure

```
course_scheduler/
├── course_scheduler/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── scheduler/                 # Main Django app
│   ├── models.py
│   ├── views.py              # Backend logic and API endpoints
│   ├── urls.py               # App URL routing
│   ├── templates/
│   │   └── scheduler/
│   │       └── home.html     # Main template
│   └── static/               # CSS and JS files
├── algorithms/               # C++ scheduling algorithm
│   ├── scheduler.cpp         # Core algorithm implementation
│   ├── input_sample.json     # Sample input data
│   ├── input_courses.json    # Generated input for algorithm
│   └── output_order.json     # Algorithm output
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
└── README.md
```

## 🔍 Algorithm Details

The scheduling algorithm implements a sophisticated approach to course sequencing:

1. **Topological Sorting**: Uses Kahn's algorithm to resolve prerequisite dependencies
2. **Graph Construction**: Builds a directed acyclic graph (DAG) from course prerequisites
3. **Optimal Ordering**: Generates semester-by-semester course sequences
4. **Cycle Detection**: Handles circular dependencies gracefully

### Key Features:
- **Time Complexity**: O(V + E) where V is courses and E is prerequisite relationships
- **Space Complexity**: O(V + E) for graph storage
- **Robustness**: Handles missing prerequisites and invalid inputs

## 🧪 Testing

### Backend Tests
```bash
python manage.py test scheduler
```

### Algorithm Testing
```bash
cd algorithms
# Test with sample input
./scheduler  # or scheduler.exe on Windows
```

### Manual Testing
- Test course selection and schedule generation
- Verify prerequisite inclusion
- Check error handling for invalid inputs

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 API Documentation

### GET /generate/
Returns a sample schedule using default input data.

**Response:**
```json
{
  "order": ["CS101", "MATH201", "CS201", "CS301"],
  "semesters": 2
}
```

### POST /generate/
Generates a custom schedule based on selected courses.

**Request Body:**
```json
{
  "courses": [
    {"code": "CS201"},
    {"code": "MATH201"}
  ]
}
```

**Response:**
```json
{
  "order": ["CS101", "MATH201", "CS201"],
  "semesters": 2
}
```

## 🔒 Security Considerations

- Input validation on all API endpoints
- CSRF protection (can be enabled by removing `@csrf_exempt`)
- Sanitized subprocess execution
- File path validation to prevent directory traversal

## 🚀 Deployment

### Local Development
```bash
python manage.py runserver
```

### Production Deployment
1. Set `DEBUG = False` in settings.py
2. Configure static file serving
3. Set up a production web server (nginx + gunicorn)
4. Use environment variables for sensitive settings

## 📈 Performance Optimizations

- **Algorithm Efficiency**: C++ implementation for fast computation
- **Lazy Loading**: Courses loaded on-demand
- **Caching**: Static file caching for improved load times
- **Database Indexing**: Optimized queries for course data

## 🐛 Known Issues & Future Improvements

- [ ] Add user authentication and personalized schedules
- [ ] Implement course conflict detection
- [ ] Add support for variable credit hours
- [ ] Create a REST API for mobile app integration
- [ ] Add comprehensive unit tests
- [ ] Implement caching for frequently accessed data

⭐ **Star this repo if you found it helpful!**
