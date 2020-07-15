from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
TYPE_CHOICES = [
   ('Teacher', 'Teacher'),
   ('Student', 'Student'),
   ('Admin','Admin')
]

class ClassName(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name


class User(AbstractUser):
    type = models.CharField(max_length = 20, choices = TYPE_CHOICES , default = 'Student')
    rollno = models.CharField(max_length = 50, null = True)
    class_name = models.ForeignKey(ClassName, on_delete = models.CASCADE,null = True)

    def __str__(self):
        return '%s %s' % (self.first_name,self.last_name)

class Subject(models.Model):
    dept = models.CharField(max_length = 50)
    subject_name = models.CharField(max_length = 100)
    subject_code = models.CharField(max_length = 20)

    def __self__(self):
        return '%s : %s' % (self.subject_code,self.subject_name)