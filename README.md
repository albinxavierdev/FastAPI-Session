# FastAPI + SQLite Task

This task will help you practice working with a database and serving it through a FastAPI API.

---

## 📌 Task Description

You need to create a **simple SQLite database** and connect it with a **FastAPI application**. The goal is to fetch student data from the database and return it as JSON through an API endpoint.

---

## 📝 Steps

### 1. Set up SQLite
- Use SQLite (built into Python, no installation required).
- Create a database file named `students.db`.

### 2. Create a Table
- Inside the database, create a table named `students` with the following fields:
  - `id` (Primary Key, Auto Increment)
  - `name` (Text)
  - `age` (Integer)
  - `course` (Text)

### 3. Insert Sample Data
- Add at least **5 student records** into the `students` table.

### 4. Connect FastAPI to SQLite
- In your FastAPI project, configure a connection to `students.db`.
- Ensure your app can query data from the `students` table.

### 5. Build an API Endpoint
- Create an endpoint `/students` that returns **all student records** in JSON format.

### 6. Test the API
- Run the FastAPI app.
- Open `/students` in a browser or test with Postman/`curl`.
- Verify that all student records are returned in JSON.

---

## 🚀 Extension Task (Optional)
- Add an endpoint `/students/{id}` to return the details of a **single student** by ID.
- Handle the case where the student does not exist.

---

## ✅ Deliverables
- A working `students.db` SQLite database.
- A FastAPI project with at least one working endpoint (`/students`).
- JSON output of student data.

---
