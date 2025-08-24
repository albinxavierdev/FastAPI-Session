from fastapi import FastAPI
import sqlite3

app = FastAPI()

@app.get("/students")
def read_students():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    
    
    students = []
    for row in rows:
        students.append({
            "id": row[0],
            "name": row[1],
            "age": row[2],
            "course": row[3]
        })
    return students