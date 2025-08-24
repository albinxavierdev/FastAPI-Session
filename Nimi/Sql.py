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
    ('Nimi', 20, 'Math'),
    ('Riya', 22, 'Physics'),
    ('cheni', 19, 'Chemistry'),
    ('yash', 21, 'Biology'),
    ('krish', 23, 'Computer Science')
])

conn.commit()
conn.close()
print("Database created and sample data added!")