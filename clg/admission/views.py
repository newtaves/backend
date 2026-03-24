from django.shortcuts import render, redirect
from django.contrib import messages
from .models import StudentApplication
from core.models import Department, Course

def index(request):
    return render(request, 'admission/index.html')

def apply(request):
    departments = Department.objects.all()
    courses = Course.objects.all()
    
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dept_id = request.POST.get('department')
        course_id = request.POST.get('course')
        marks = request.POST.get('marks')
        
        try:
            dept = Department.objects.get(id=dept_id)
            course = Course.objects.get(id=course_id)
            
            StudentApplication.objects.create(
                full_name=full_name,
                email=email,
                phone=phone,
                department=dept,
                course=course,
                high_school_marks=marks
            )
            messages.success(request, "Your application has been submitted successfully!")
            return render(request, 'admission/success.html', {'name': full_name})
        except Exception as e:
            messages.error(request, f"Error submitting application: {e}")
            
    return render(request, 'admission/apply.html', {
        'departments': departments,
        'courses': courses
    })