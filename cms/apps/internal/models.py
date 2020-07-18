
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import math
from django.conf import settings
from apps.authentication.models import Subject,Classroom
# Create your models here

class Mark(models.Model):
    internal_1 = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(20)])
    internal_2 = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(20)])
    assignment_1 = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(10)])
    assignment_2 = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(10)])
    subject  = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Internal(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE )
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    clas = models.ForeignKey(Classroom, on_delete=models.CASCADE)

class Assignment(models.Model):
    asn_name = models.CharField(max_length=200,null =True)
    due_date = models.DateField(null= True)
    desc =models.TextField(null= True)
    subject =models.ForeignKey(Subject,on_delete=models.CASCADE )
    clas = models.ForeignKey(Classroom,on_delete= models.CASCADE)