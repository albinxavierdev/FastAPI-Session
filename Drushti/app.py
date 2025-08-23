from fastapi import FastAPI, HTTPException
import sqlite3

app = FastAPI()

# Function to connect to DB
def get_db_connection():
    conn = sqlite3.connect("students.db")
    conn.row_factory = sqlite3.Row  # So we can return dict-like rows
    return conn

@app.get("/")
def root():
    return {"message": "FastAPI with SQLite is running!"}

@app.get("/students")
def get_students():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()

    # Convert rows to list of dicts
    students = [dict(row) for row in rows]
    return {"students": students}

@app.get("/students/{student_id}")
def get_student(student_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE Student_ID = ?", (student_id,))
    row = cursor.fetchone()
    conn.close()

    if row is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return dict(row)
