from django.shortcuts import render ,redirect
from .models import Internal,Mark,TeacherAssignment,StudentAssignment
from apps.authentication.models import User,Classroom,Subject
from django.http import HttpResponseRedirect,HttpResponse
from .forms import TassignmentForm, SassignmentForm
# Create your views here.
#teacher classes
def tclass(request):
    classes= Internal.objects.filter(teacher__first_name='Ajith')
    return render(request,'internal/teacher_class.html',{'tclass':classes})
#teacher enter marks
def entermark(request,subid,clasid):
    if request.method=="GET":
        mark= Mark.objects.filter(subject__id=subid,student__class_name=clasid)
        context={
            'mark': mark,
            'class':Classroom.objects.get(id=clasid),
            'subject':Subject.objects.get(id=subid),
            'classname' : request.user.class_name,
        }
        return render(request,'internal/marks_enter.html',context)
    if request.method=="POST":
        count = len(request.POST.getlist("internal1"))
        for i in range(count):
            internal_1=int(request.POST.getlist("internal1")[i])
            internal_2=int(request.POST.getlist("internal2")[i])
            assignment_1=int(request.POST.getlist("assignment1")[i])
            assignment_2=int(request.POST.getlist("assignment2")[i] )
            sid = request.POST.getlist("studentid")[i]
            total= internal_1+internal_2+assignment_1+assignment_2
            m= Mark.objects.get(subject__id=subid,student__id=sid)
            m.internal_1= internal_1
            m.internal_2=internal_2
            m.assignment_1=assignment_1
            m.assignment_2=assignment_2
            m.total= total
            m.save()
        return HttpResponseRedirect('')
#student view marks          
def viewmarks(request):
    context={
        'mark':Mark.objects.filter(student=request.user),
        'student':User.objects.get(rollno=request.user.rollno)
    }    
    return render(request,'internal/marks_view.html',context)
  
#teacher assignment
def tassignment(request,subid,clasid):
    sub= Subject.objects.get(id=subid)
    clas= Classroom.objects.get(id=clasid)
    if request.method=='POST':
        form=TassignmentForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.subject= sub
            post.class_room =clas
            post.save()
            return  HttpResponseRedirect('')
    else:
            form= TassignmentForm()
            context={
                'form':form
            }
    return render(request,'internal/teacherassignment.html',context)                                               
#student assignment list view
def studassignview(request):
   context={
        'studassignment': StudentAssignment.objects.filter(student__rollno=request.user.rollno),
   }   
   return render(request,'internal/studassignment_view.html',context)
  

def studassignsubmit(request,aid):
    studassignment =StudentAssignment.objects.get(id=aid)
    if request.method=='POST':
        form=SassignmentForm(request.POST or None,request.FILES or None,instance= studassignment)
        if form.is_valid():
            post=form.save(commit=False)
            post.status="Submitted"
            post.save()

    else:
       
        form= SassignmentForm()
    context={
        'form':form,
        'studas': studassignment
     }       
    return render(request,'internal/assignmentsubmit.html',context)
     
def tassignview(request,subid,clasid):
    studassignment= StudentAssignment.objects.filter(assignment__subject=subid,assignment__class_room=clasid,status="Submitted")
    context ={
        'studas':studassignment,
        'class':Classroom.objects.get(id=clasid),
        'subject':Subject.objects.get(id=subid),
        'classname' : request.user.class_name,
}
    return render(request,'internal/tassignview.html',context)