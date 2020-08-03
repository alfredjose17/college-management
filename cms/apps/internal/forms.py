from django import forms
from .models import TeacherAssignment,StudentAssignment
class TassignmentForm(forms.ModelForm):
    class Meta:
        model= TeacherAssignment
        fields =[
            'assignment_name',
            'due_date',
            'description',
            'question'
        ]
        labels= {
            'assignment_name':'ASSIGNMENT NAME',
            'due_date':'DUE DATE',
            'description':'DESCRIPTION',
            'question':'QUESTION',
        }
class SassignmentForm(forms.ModelForm):
     class Meta:
        model= StudentAssignment
        fields =[
            'answer',
        ]
        labels={
            'answer':'Your Work',
        }

