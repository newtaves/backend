
from django import forms
from .models import StudentApplication

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = StudentApplication
        # These are the fields the student will see
        fields = ['full_name', 'email', 'phone', 'high_school_marks', 'course']
        # This makes the form look a bit nicer
        widgets = {
        'full_name': forms.TextInput(attrs={'placeholder': 'Enter your full name'}),
        'email': forms.EmailInput(attrs={'placeholder': 'example@mail.com'}),
        }