# create_db.py
import sqlite3

# Connect to SQLite (will create students.db if not exists)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    course TEXT NOT NULL
)
""")

# Insert sample data
students = [
    ("Amit", 21, "Computer Science"),
    ("Riya", 22, "Mathematics"),
    ("Karan", 20, "Physics"),
    ("Sneha", 23, "Chemistry"),
    ("Arjun", 21, "Economics"),
]

cursor.executemany("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", students)

conn.commit()
conn.close()

print("Database and sample data created successfully!")
