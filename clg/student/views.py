from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Student, Enrollment

@login_required
def dashboard(request):
    try:
        student = request.user.student_profile
        enrollments = student.enrollments.all()
        return render(request, 'student/dashboard.html', {
            'student': student,
            'enrollments': enrollments
        })
    except Student.DoesNotExist:
        return render(request, 'student/dashboard.html', {'error': 'Student profile not found.'})
