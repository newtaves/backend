from django.db import models
from core.models import Department, Course

class StudentApplication(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]

    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    high_school_marks = models.DecimalField(max_digits=5, decimal_places=2)
    phone = models.CharField(max_length=15)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return f"{self.full_name} - {self.course.name}"