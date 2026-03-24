from django.db import models
from core.models import Department, User

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='teachers')
    hire_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username
