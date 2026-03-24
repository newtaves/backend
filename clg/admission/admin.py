from django.contrib import admin
from . import models
from student.models import Student, Enrollment
from core.models import User

@admin.action(description="Admit selected applicants as students")
def admit_students(modeladmin, request, queryset):
    for app in queryset:
        if app.status != 'APPROVED':
            # Create a user for the new student
            username = app.email.split('@')[0]
            # Handle possible duplicate usernames
            count = User.objects.filter(username__startswith=username).count()
            if count > 0:
                username = f"{username}{count}"
            
            user = User.objects.create_user(
                username=username,
                email=app.email,
                password="password123", # Set a default
                role=User.Role.STUDENT
            )
            
            # Create Student record
            student = Student.objects.create(
                user=user,
                name=app.full_name,
                email=app.email,
                department=app.department,
                high_school_marks=app.high_school_marks,
                mobile_number=app.phone
            )
            
            # Enroll the student in the requested course
            Enrollment.objects.create(
                student=student,
                course=app.course,
            )
            
            # Mark app as approved
            app.status = 'APPROVED'
            app.save()

@admin.register(models.StudentApplication)
class StudentApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'course', 'status')
    list_filter = ('status', 'department')
    actions = [admit_students]