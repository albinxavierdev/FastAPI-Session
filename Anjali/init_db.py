import sqlite3
import os
import sys

def init_database():
    try:
        # Get current working directory
        current_dir = os.getcwd()
        db_path = os.path.join(current_dir, "students.db")
        
        print(f"🔄 Current working directory: {current_dir}")
        print(f"🔄 Database will be created at: {db_path}")
        
        # Connect (creates students.db in the same folder if not exists)
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        print("✅ Connected to SQLite database")
        
        # Create table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            course TEXT NOT NULL
        )
        """)
        
        print("✅ Students table created/verified")
        
        # Insert sample data (only if table is empty)
        cursor.execute("SELECT COUNT(*) FROM students")
        count = cursor.fetchone()[0]
        print(f"📊 Current student count: {count}")
        
        if count == 0:
            sample_data = [
                ("Alice", 20, "Computer Science"),
                ("Bob", 22, "Mathematics"),
                ("Charlie", 21, "Physics"),
                ("David", 23, "Chemistry"),
                ("Eva", 19, "Biology")
            ]
            
            cursor.executemany("""
            INSERT INTO students (name, age, course) VALUES (?, ?, ?)
            """, sample_data)
            
            print(f"✅ Inserted {len(sample_data)} sample students")
        else:
            print("ℹ️  Table already contains data, skipping sample insertion")
        
        conn.commit()
        conn.close()
        
        # Verify file was created
        if os.path.exists(db_path):
            file_size = os.path.getsize(db_path)
            print(f"✅ Database file created successfully!")
            print(f"📁 File size: {file_size} bytes")
            print(f"📁 File path: {db_path}")
        else:
            print("❌ ERROR: Database file was not created!")
            
    except sqlite3.Error as e:
        print(f"❌ SQLite error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    print("🚀 Starting database initialization...")
    init_database()
    print("🎉 Database initialization completed!")
