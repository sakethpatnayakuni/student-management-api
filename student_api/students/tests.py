from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Student


class StudentTest(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.student = Student.objects.create(
            id="1",
            name="Test User",
            age=20,
            enroll_date="2024-01-01"
        )

    
    def test_create_student(self):
        data = {
            "id": "2",
            "name": "New Student",
            "age": 22,
            "enroll_date": "2024-02-01"
        }
        response = self.client.post('/students/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    
    def test_list_students(self):
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    def test_get_student(self):
        response = self.client.get(f'/students/{self.student.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    def test_update_student(self):
        data = {
            "id": "1",
            "name": "Updated Name",
            "age": 25,
            "enroll_date": "2024-01-01"
        }
        response = self.client.put(f'/students/{self.student.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    def test_delete_student(self):
        response = self.client.delete(f'/students/{self.student.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

   
    def test_student_not_found(self):
        response = self.client.get('/students/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
