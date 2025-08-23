# create_db.py
import sqlite3

# Connect to SQLite (creates file if not exists)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Student_ID INTEGER NOT NULL,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    course TEXT NOT NULL
)
""")

# Insert sample data
students = [
    (1, "Alice", 21, "Computer Science"),
    (2, "Bob", 22, "Mathematics"),
    (3, "Charlie", 20, "Physics"),
    (4, "David", 23, "Economics"),
    (5, "Eva", 21, "Biology")
]

cursor.executemany("INSERT INTO students (Student_ID, name, age, course) VALUES (?, ?, ?, ?)", students)

conn.commit()
conn.close()

print("Database and sample data created successfully.")
