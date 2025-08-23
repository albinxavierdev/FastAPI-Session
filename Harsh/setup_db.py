import sqlite3

# Connect to database (it will create it if not exists)
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT
)
''')

# Add 5 students
cursor.executemany('''
INSERT INTO students (name, age, course)
VALUES (?, ?, ?)
''', [
    ('Alice', 20, 'Math'),
    ('Bob', 22, 'Physics'),
    ('Charlie', 19, 'Chemistry'),
    ('Diana', 21, 'Biology'),
    ('Ethan', 23, 'Computer Science')
])

conn.commit()
conn.close()
print("Database created and sample data added!")
