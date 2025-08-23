from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
import os
from typing import List, Optional

app = FastAPI(title="Student Management API", version="1.0.0")

# Database connection
def get_db_connection():
    db_path = os.path.join(os.getcwd(), "students.db")
    if not os.path.exists(db_path):
        raise HTTPException(status_code=500, detail="Database not found. Please run init_db.py first.")
    return sqlite3.connect(db_path)

# Pydantic models
class StudentBase(BaseModel):
    name: str
    age: int
    course: str

class Student(StudentBase):
    id: int
    
    class Config:
        from_attributes = True

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    course: Optional[str] = None

# Routes
@app.get("/")
async def root():
    return {"message": "Student Management API", "status": "running"}

@app.get("/students", response_model=List[Student])
async def get_students():
    """Get all students"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, age, course FROM students")
    students = cursor.fetchall()
    conn.close()
    
    return [Student(id=row[0], name=row[1], age=row[2], course=row[3]) for row in students]

@app.get("/students/{student_id}", response_model=Student)
async def get_student(student_id: int):
    """Get a specific student by ID"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, age, course FROM students WHERE id = ?", (student_id,))
    student = cursor.fetchone()
    conn.close()
    
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    return Student(id=student[0], name=student[1], age=student[2], course=student[3])

@app.post("/students", response_model=Student)
async def create_student(student: StudentCreate):
    """Create a new student"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
        (student.name, student.age, student.course)
    )
    student_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return Student(id=student_id, name=student.name, age=student.age, course=student.course)

@app.put("/students/{student_id}", response_model=Student)
async def update_student(student_id: int, student_update: StudentUpdate):
    """Update a student"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Get current student data
    cursor.execute("SELECT id, name, age, course FROM students WHERE id = ?", (student_id,))
    current = cursor.fetchone()
    if not current:
        conn.close()
        raise HTTPException(status_code=404, detail="Student not found")
    
    # Update only provided fields
    name = student_update.name if student_update.name is not None else current[1]
    age = student_update.age if student_update.age is not None else current[2]
    course = student_update.course if student_update.course is not None else current[3]
    
    cursor.execute(
        "UPDATE students SET name = ?, age = ?, course = ? WHERE id = ?",
        (name, age, course, student_id)
    )
    conn.commit()
    conn.close()
    
    return Student(id=student_id, name=name, age=age, course=course)

@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    """Delete a student"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Student not found")
    
    conn.commit()
    conn.close()
    
    return {"message": f"Student {student_id} deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
