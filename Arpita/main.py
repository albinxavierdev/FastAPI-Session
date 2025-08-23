import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# ---------------------------
# Database Setup (SQLite)
# ---------------------------
def init_db():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        course TEXT NOT NULL
    )
    """)

    # Insert sample data (only if table is empty)
    cursor.execute("SELECT COUNT(*) FROM students")
    if cursor.fetchone()[0] == 0:
        sample_data = [
            ("Arpita kaushal", 22, "Data Science"),
            ("Harshita jain", 21, "Cybersecurity"),
            ("Priya Verma", 23, "AI & ML"),
            ("Rohit Singh", 20, "Web Development"),
            ("Neha Gupta", 22, "Cloud Computing")
        ]
        cursor.executemany("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", sample_data)
        conn.commit()

    conn.close()


# ---------------------------
# FastAPI App
# ---------------------------
app = FastAPI()

# Initialize database when app starts
init_db()


# Pydantic model for input validation
class Student(BaseModel):
    name: str
    age: int
    course: str


# Helper function to fetch all students
def fetch_all_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()

    students = [{"id": r[0], "name": r[1], "age": r[2], "course": r[3]} for r in rows]
    return students


# Helper function to fetch student by ID
def fetch_student_by_id(student_id: int):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return {"id": row[0], "name": row[1], "age": row[2], "course": row[3]}
    return None


# ---------------------------
# API Endpoints
# ---------------------------

@app.get("/students")
def get_students():
    """Fetch all students"""
    return fetch_all_students()


@app.get("/students/{student_id}")
def get_student(student_id: int):
    """Fetch a student by ID"""
    student = fetch_student_by_id(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@app.post("/students")
def add_student(student: Student):
    """Add a new student"""
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", 
                   (student.name, student.age, student.course))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return {"id": new_id, "name": student.name, "age": student.age, "course": student.course}