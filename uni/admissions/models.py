from django.db import models
from core.models import Department

class StudentApplication(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    high_school_marks = models.DecimalField(max_digits=5, decimal_places=2)
    course = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name