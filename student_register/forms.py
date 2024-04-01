from django import forms
from .models import student_register

class  StudentRegisterForm(forms.ModelForm):
    class Meta:
        model = student_register
        fields="__all__"
        