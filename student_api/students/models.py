from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.CharField(primary_key=True,max_length=20)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    enroll_date = models.DateField()

    def __str__(self):
        return self.name