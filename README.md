# Student Management System API

A Django REST API with a simple UI to manage student records. Supports CRUD operations, search, CSV export, validation, and error handling.

---

##  Features

* Add new students (ID, Name, Age, Enrollment Date)
* Retrieve student details
* Update student information
* Delete student records
* List all students
* Search students by Name or ID
* Export student data to CSV
* Input validation (Age: 1–100)
* Error handling (404 for not found)
* Admin panel support

---

##  Tech Stack

* Python
* Django
* Django REST Framework
* HTML, CSS

---

##  Setup Instructions

1. Clone the repository:
   git clone https://github.com/sakethpatnayakuni/student-management-api.git

2. Navigate to project folder:
   cd student_api_project

3. Create virtual environment:
   python -m venv venv

4. Activate virtual environment:
   venv\Scripts\activate

5. Install dependencies:
   pip install -r requirements.txt

6. Run migrations:
   python manage.py migrate

7. Start server:
   python manage.py runserver

---

##  URLs

* Home Page: http://127.0.0.1:8000/
* UI Page: http://127.0.0.1:8000/ui/
* API: http://127.0.0.1:8000/students/
* Admin Panel: http://127.0.0.1:8000/admin/
* Export CSV: http://127.0.0.1:8000/export/

---

##  Testing

Run tests:
python manage.py test

---

##  Security

* SECRET_KEY is managed using environment variables.

---

##  Notes

* Custom string ID is used for student identification.
* Validation ensures age is between 1 and 100.

---

##  Author

Saketh Patnayakuni
