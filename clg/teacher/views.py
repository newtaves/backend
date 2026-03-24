from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from student.models import Student, Enrollment
from teacher.models import Teacher

@login_required
def dashboard(request):
    # Ensure user is a teacher
    if not hasattr(request.user, 'teacher_profile'):
        messages.error(request, "Access denied. Teacher profile not found.")
        return redirect('admission:index')
    
    teacher = request.user.teacher_profile
    # For now, let's show all students in the teacher's department
    students = Student.objects.filter(department=teacher.department)
    
    return render(request, 'teacher/dashboard.html', {
        'teacher': teacher,
        'students': students
    })

@login_required
def update_grade(request, enrollment_id):
    enrollment = get_object_or_404(Enrollment, id=enrollment_id)
    
    # Check if the teacher belongs to the same department as the student's course
    if not hasattr(request.user, 'teacher_profile') or \
       request.user.teacher_profile.department != enrollment.course.department:
        messages.error(request, "You don't have permission to grade this student.")
        return redirect('teacher:dashboard')

    if request.method == 'POST':
        marks = request.POST.get('marks')
        try:
            enrollment.marks = marks
            enrollment.save()
            messages.success(request, f"Updated grade for {enrollment.student.name}")
            return redirect('teacher:dashboard')
        except Exception as e:
            messages.error(request, f"Error updating grade: {e}")

    return render(request, 'teacher/update_grade.html', {
        'enrollment': enrollment
    })
