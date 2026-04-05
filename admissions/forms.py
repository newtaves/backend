from django import forms
from .models import StudentApplication
from core.models import Department


class AdmissionForm(forms.ModelForm):
    course = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        empty_label="Select Course"
    )

    class Meta:
        model = StudentApplication
        fields = ['full_name', 'email', 'phone', 'high_school_marks', 'course']

        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Enter your full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'example@mail.com'}),
        }