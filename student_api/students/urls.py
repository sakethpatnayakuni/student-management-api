from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, edit_student, export_students_csv,student_list,delete_student,home

router = DefaultRouter()
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('', home, name='home'),   
] + router.urls + [
    path('students/export/', export_students_csv, name='export_students_csv'),
    path('ui/', student_list, name='student_ui'),
    path('delete/<str:id>/', delete_student, name='delete_student'),
    path('edit/<str:id>/', edit_student, name='edit_student'),
]
