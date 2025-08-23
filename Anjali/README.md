# FastAPI + SQLite Student Management System

A simple REST API built with FastAPI and SQLite for managing student records. This project demonstrates basic CRUD operations using FastAPI with a SQLite database.

## 🚀 Features

- **Get All Students**: Retrieve a list of all students
- **Get Student by ID**: Retrieve a specific student by their ID
- **SQLite Database**: Lightweight, file-based database
- **RESTful API**: Clean HTTP endpoints following REST principles
- **Error Handling**: Proper HTTP status codes and error messages

## 🛠️ Tech Stack

- **FastAPI** - Modern, fast web framework for building APIs
- **SQLite** - Lightweight, serverless database
- **Python** - Programming language
- **Uvicorn** - ASGI server for running FastAPI

## 📋 Prerequisites

- Python 3.7+ installed on your system
- pip (Python package installer)

## 🚀 Installation & Setup

### 1. Clone or Download the Project
```bash
# If using git
git clone <repository-url>
cd "FastAPI + SQLite Task"

# Or simply download and extract the project files
```

### 2. Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv v
v\Scripts\activate

# macOS/Linux
python3 -m venv v
source v/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Initialize Database
```bash
python init_db.py
```
This will create a `students.db` file with sample student data.

### 5. Run the Application
```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

## 📚 API Endpoints

### Get All Students
```http
GET /students
```

**Response:**
```json
[
  {
    "id": 1,
    "name": "Alice",
    "age": 20,
    "course": "Computer Science"
  },
  {
    "id": 2,
    "name": "Bob",
    "age": 22,
    "course": "Mathematics"
  }
]
```

### Get Student by ID
```http
GET /students/{student_id}
```

**Parameters:**
- `student_id` (integer): The unique identifier of the student

**Response:**
```json
{
  "id": 1,
  "name": "Alice",
  "age": 20,
  "course": "Computer Science"
}
```

**Error Response (404):**
```json
{
  "detail": "Student not found"
}
```

## 🗄️ Database Schema

The `students` table has the following structure:

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | INTEGER | PRIMARY KEY, AUTOINCREMENT | Unique student identifier |
| `name` | TEXT | NOT NULL | Student's full name |
| `age` | INTEGER | NOT NULL | Student's age |
| `course` | TEXT | NOT NULL | Student's course of study |

## 📖 Sample Data

The database comes pre-populated with sample students:

- Alice, 20, Computer Science
- Bob, 22, Mathematics
- Charlie, 21, Physics
- David, 23, Chemistry
- Eva, 19, Biology

## 🔧 Development

### Project Structure
```
FastAPI + SQLite Task/
├── main.py              # FastAPI application and endpoints
├── init_db.py           # Database initialization script
├── requirements.txt     # Python dependencies
├── students.db          # SQLite database file (created after init)
└── README.md           # This file
```

### Adding New Endpoints

To add new endpoints, modify `main.py`:

```python
@app.post("/students")
def create_student(name: str, age: int, course: str):
    # Implementation here
    pass
```

### Database Operations

The project uses raw SQL queries. For more complex operations, consider using an ORM like SQLAlchemy.

## 🌐 API Documentation

Once the server is running, you can access:

- **Interactive API docs**: `http://127.0.0.1:8000/docs`
- **Alternative docs**: `http://127.0.0.1:8000/redoc`

## 🧪 Testing the API

### Using curl
```bash
# Get all students
curl http://127.0.0.1:8000/students

# Get student by ID
curl http://127.0.0.1:8000/students/1
```

### Using the Interactive Docs
1. Open `http://127.0.0.1:8000/docs` in your browser
2. Click on any endpoint to expand it
3. Click "Try it out" to test the endpoint
4. Click "Execute" to see the response

## 🚨 Error Handling

The API includes proper error handling:
- **404 Not Found**: When a student ID doesn't exist
- **500 Internal Server Error**: For database connection issues

## 🔒 Security Notes

- This is a development/demo project
- No authentication or authorization implemented
- Database file is stored locally
- Consider adding input validation for production use

## 🚀 Future Enhancements

- [ ] Add POST endpoint to create new students
- [ ] Add PUT endpoint to update student information
- [ ] Add DELETE endpoint to remove students
- [ ] Implement input validation with Pydantic models
- [ ] Add search and filtering capabilities
- [ ] Implement pagination for large datasets
- [ ] Add authentication and authorization
- [ ] Add logging and monitoring

## 🤝 Contributing

Feel free to contribute to this project by:
- Adding new features
- Improving error handling
- Enhancing documentation
- Adding tests

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

If you encounter any issues:
1. Check that all dependencies are installed
2. Ensure the database is initialized
3. Verify the server is running
4. Check the console for error messages

---

**Happy Coding! 🎉**
