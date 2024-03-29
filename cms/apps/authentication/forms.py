from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

TYPE_CHOICES = [
   ('teacher', 'Teacher'),
   ('student', 'Student'),
   ('admin','Admin'),
]

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields =  ('username','email','type','rollno','class_name')


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('username','email','type','rollno','class_name')
