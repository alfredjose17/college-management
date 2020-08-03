from django.shortcuts import render ,redirect
from .models import Attendance
from apps.authentication.models import User,Classroom,Subject
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
def enterattendance(request,subid,clasid):
    if request.method=="GET":        
        attendance= Attendance.objects.filter(subject__id=subid,student__class_name=clasid)
        context={
            'attendance': attendance,
            'subject': Subject.objects.get(id=subid), 
        }
        return render(request,'attendance/attendance_enter.html',context)
    if request.method=="POST":
        print("debug",(request.POST))
        count = len(request.POST.getlist("status"))
        for i in range(count):
            status=request.POST.getlist("status")[i]
            sid = request.POST.getlist("studentid")[i]
            a= Attendance.objects.get(subject__id=subid,student__id=sid)
            pcount = a.presentcount
            tcount = a.totcount
            if status=='True':
                pcount += 1
            tcount += 1
            total = (pcount/tcount)*100
            a.presentcount = pcount
            a.totcount = tcount
            a.total = total            
            a.save()
        return HttpResponseRedirect('')
#student view attendance
def viewattendance(request):
    context={
        'attendance':Attendance.objects.filter(student__rollno=request.user.rollno),
        'student':User.objects.get(rollno=request.user.rollno)
    }    
    return render(request,'attendance/attendance_view.html',context)
