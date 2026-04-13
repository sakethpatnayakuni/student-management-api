from django.shortcuts import render,redirect


# Create your views here.
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
import csv
from django.http import HttpResponse
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

def export_students_csv(request):
    response = HttpResponse(content_type = 'text/csv')
    response['content-disposition'] = 'attachement; filename="students.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID','Name','Age','Enroll_Date'])

    students = Student.objects.all().values_list('id','name','age','enroll_date')
    for student in students:
        writer.writerow([
            student.id,
            student.name,
            student.age,
            student.enroll_date
        ])
    return response
def student_list(request):
    query = request.GET.get('search') 
    if query:
        students = Student.objects.filter(
            name__icontains=query
        ) | Student.objects.filter(
            id__icontains=query
        )
    else:
        students = Student.objects.all()
    return render(request,'students/index.html',{'students':students})
def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('student_ui')
def edit_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.age = request.POST.get('age')
        student.enroll_date = request.POST.get('enroll_date')
        student.save()
        return redirect('student_ui')

    return render(request, 'students/edit.html', {'student': student})
def home(request):
    return render(request,'students/home.html')
