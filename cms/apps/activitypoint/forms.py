from django import forms
from .models import Activitypoint

class ActivityForm(forms.ModelForm):
    class Meta:
        model=Activitypoint
        fields=[
            'activity',
            'activitylevel',
            'prize',
            'involvement',
            'document',
            'year',
            'notes'
        ]
        labels={
            'activity':'Activity:',
            'activitylevel':'Activity Level:',
            'prize':'Prize(if any):',
            'involvement':'Involvement Level(Only for leadership & management Activities):',
            'document':'Document(File name should be ''rollno_doc_x.extension'' Eg:CS18B1_doc_2.jpg):',
            'year':'Year of completion:',
            'notes':'Notes:'
        }