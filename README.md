# Student Management System API

## Description
This is a Django-based Student Management System API that supports CRUD operations, search functionality, CSV export, and a basic HTML UI.

---

##  How to Run the Project

### 1. Clone the repository
git clone https://github.com/sakethpatnayakuni/student-management-api.git

### 2. Navigate to project folder
cd student-management-api

### 3. Create virtual environment
python -m venv venv

### 4. Activate virtual environment
venv\Scripts\activate   (Windows)

### 5. Install dependencies
pip install django djangorestframework

### 6. Apply migrations
python manage.py makemigrations
python manage.py migrate

### 7. Run server
python manage.py runserver

---

## URLs

- API: http://127.0.0.1:8000/students/
- UI: http://127.0.0.1:8000/ui/
- Export CSV: http://127.0.0.1:8000/students/export/

---

## Features
- Add, Update, Delete students
- Search by name or ID
- Export student data to CSV
- Simple UI using HTML/CSS
