from django.db import models
from core.models import Department

# Student Table
class Student(models.Model):
    name = models.CharField()
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name