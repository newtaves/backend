from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AdmissionForm


def home(request):
    return render(request, 'admissions/index.html')


def apply(request):
    if request.method == "POST":
        form = AdmissionForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Application submitted successfully!")
            return redirect('home')

    else:
        form = AdmissionForm()

    return render(request, 'admissions/apply.html', {'form': form})