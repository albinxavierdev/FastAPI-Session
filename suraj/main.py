import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT
)
''')

cursor.executemany('''
INSERT INTO students (name, age, course)
VALUES (?, ?, ?)
''', [
    ('suraj', 20, 'Math'),
    ('rahul', 22, 'Physics'),
    ('vijay', 19, 'Chemistry'),
    ('yash', 21, 'Biology'),
    ('chomu', 23, 'Computer Science')
])

conn.commit()
conn.close()
print("Database created and sample data added!")