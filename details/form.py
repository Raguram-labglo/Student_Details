from django import forms
from .models import *


class Student_form(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
    

class Mark_form(forms.ModelForm):
    
    class Meta:
        model = Mark
        fields = ['student_num','subject','mark','mail']