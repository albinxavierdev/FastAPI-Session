# main.py
from fastapi import FastAPI, HTTPException
import sqlite3

app = FastAPI()

# Function to get DB connection
def get_db_connection():
    conn = sqlite3.connect("students.db")
    conn.row_factory = sqlite3.Row  # Enables dict-like access
    return conn

# Endpoint to fetch all students
@app.get("/students")
def get_students():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()

    students = [dict(row) for row in rows]
    return {"students": students}

# Endpoint to fetch a single student by ID
@app.get("/students/{student_id}")
def get_student(student_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    row = cursor.fetchone()
    conn.close()

    if row is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return dict(row)
