
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import math
from datetime import datetime
from django.conf import settings
from apps.authentication.models import Subject,Classroom,User
from django.db.models.signals import pre_save,post_save
# Create your models here

class Mark(models.Model):
    internal_1 = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(20)])
    internal_2 = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(20)])
    assignment_1 = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(5)])
    assignment_2 = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(5)])
    total = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(50)])
    subject  = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta():
        unique_together = (('student', 'subject'),)
    def __str__(self):
        sub= Subject.objects.get(id=self.subject_id)
        return '%s'%(sub.subject_code)
class Internal(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE )
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    class_room = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    


    def __str__(self):
        cl = Classroom.objects.get(id=self.class_room_id)
        sub = Subject.objects.get(id=self.subject_id)
        te = User.objects.get(id=self.teacher_id)
        return '%s : %s : %s' % (te.first_name,sub.subject_code,cl.name)

class TeacherAssignment(models.Model):
    assignment_name = models.CharField(max_length=200)
    due_date = models.DateTimeField(default = datetime.now)
    description = models.TextField(null= True,blank=True)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE )
    class_room  = models.ForeignKey(Classroom,on_delete= models.CASCADE)
    question = models.FileField(upload_to="uploads/")

    def __str__(self):
        return (self.assignment_name)
class StudentAssignment(models.Model):
    student=  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    answer = models.FileField(upload_to="uploads/",null=True)
    assignment = models.ForeignKey(TeacherAssignment,on_delete=models.CASCADE)
    submitted_date = models.DateTimeField(null=True)
    status = models.CharField(max_length=50,default="Unsubmitted")
    def __str__(self):
        return (self.student.first_name)
#triggers
def createmarks(sender,instance,created,**kwargs):
   
    if created:
        stud= User.objects.filter(class_name=instance.class_room,type='student')
        for s in stud :
            try:
                Mark.objects.get(student=s, subject=instance.subject)
            except Mark.DoesNotExist:
                Mark.objects.create(student=s,subject=instance.subject)
            print('Marks created')
#post_save.connect(createmarks, sender= Internal)    

def screatemarks(sender,instance,created,**kwargs):
    if created == False:
        sub= Internal.objects.filter(class_room=instance.class_name)
        for s in sub:
            if instance.type=="student":
                try:
                    Mark.objects.get(student=instance, subject=s.subject)
                except Mark.DoesNotExist:
                    Mark.objects.create(student=instance,subject=s.subject)
        print('Marks created')
def studassignment(sender,instance,created,**kwargs):
    if created:
        stud= User.objects.filter(class_name=instance.class_room,type="student")
        for s in stud :
            StudentAssignment.objects.create(student=s,assignment=instance)        
post_save.connect(screatemarks,sender=User)
post_save.connect(createmarks, sender= Internal) 
post_save.connect(studassignment, sender= TeacherAssignment) 
