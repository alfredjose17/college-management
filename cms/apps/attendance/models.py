from django.db import models
from django.conf import settings
from apps.authentication.models import Subject

# Create your models here.

class Attendance(models.Model):
    subject  = models.ForeignKey(Subject, on_delete=models.CASCADE)
    present = models.BooleanField(null = True)
    total = models.BooleanField(default = 'True')
    date = models.DateField(null = True)
    student = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
