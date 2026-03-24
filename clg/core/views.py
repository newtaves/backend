from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def redirect_dashboard(request):
    if request.user.role == 'STUDENT':
        return redirect('student:dashboard')
    elif request.user.role == 'TEACHER':
        return redirect('teacher:dashboard')
    return redirect('admission:index')
