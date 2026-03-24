from django.shortcuts import render, redirect
from .forms import AdmissionForm


def home(request):
    return render(request, 'admissions/index.html')


def apply(request):
    if request.method == "POST":
        form = AdmissionForm(request.POST)
        if form.is_valid():
            form.save()  # Save data to database
            return redirect('success')
    else:
        form = AdmissionForm()

    return render(request, 'admissions/apply.html', {'form': form})


def success(request):
    return render(request, 'admissions/success.html')