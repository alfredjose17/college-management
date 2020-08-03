from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import math
from datetime import datetime
from django.conf import settings
from apps.authentication.models import Subject,Classroom,User
from django.db.models.signals import pre_save,post_save
from apps.internal.models import  Internal
# Create your models here.

class Attendance(models.Model):
    subject  = models.ForeignKey(Subject, on_delete=models.CASCADE)
    present = models.BooleanField(default= True)
    total = models.FloatField(default =0)
    date = models.DateField(null = True,blank=True)
    student = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    presentcount = models.IntegerField(default=0)
    totcount =models.IntegerField(default=0)

#triggers

def createattendance(sender,instance,created,**kwargs):   
    print("debug","hello")
    if created:
        stud= User.objects.filter(class_name=instance.class_room,type="student")
        for s in stud :
            try:
                Attendance.objects.get(student=s, subject=instance.subject)
            except Attendance.DoesNotExist:
                Attendance.objects.create(student=s,subject=instance.subject)
    

def screateattendance(sender,instance,created,**kwargs):
    print("debug","hello")
    if created == False:
        if instance.type=="student":
            sub= Internal.objects.filter(class_room=instance.class_name)
            for s in sub:
                try:
                    Attendance.objects.get(student=instance, subject=s.subject)
                except Attandence.DoesNotExist:
                    Attendance.objects.create(student=instance,subject=s.subject)
      
post_save.connect(screateattendance,sender=User)
post_save.connect(createattendance, sender= Internal)