from django import forms
from Testapp import models

class StudentModelForm(forms.ModelForm):
    class Meta:
        model=models.Student
        fields='__all__'

        