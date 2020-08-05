from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .forms import ActivityForm
from .models import Activitypoint

# Create your views here.
def student_activity_view(request):
    if request.method=='POST':   
        form=ActivityForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.student = request.user
            post.save()
            return redirect('studenthome')
    else:
        form=ActivityForm()
    context={
        'form':form
    }
    return render(request,'activitypoint/home.html',context)
def activity_list_view(request):
    c=request.user.class_name
    n=request.user
    queryset=Activitypoint.objects.filter(student__class_name__name=request.user.class_name,status="pending")
    context={
        'object_list':queryset,
        'class':c,
        'name':n
    }
    return render(request,'activitypoint/view.html',context)
def update_points(request,pk):
    if request.method=="POST":
        if request.POST['points']=="":
            status=request.POST['status']
            updation=Activitypoint.objects.filter(id=pk).update(status=status)
            return redirect('view')
        else:
            points=request.POST['points']
            status=request.POST['status']
            updation=Activitypoint.objects.filter(id=pk).update(points=points,status=status)
            return redirect('view')
def student_home_view(request):
    n=request.user
    c=request.user.class_name
    queryset=Activitypoint.objects.filter(student=request.user)    
    context={
        'object':queryset,
        'name':n,
        'class':c

    }
    return render(request,'activitypoint/studenthome.html',context)
def delete_point(request,pk):
    if request.method=="POST":
        dele=Activitypoint.objects.get(id=pk)
        dele.delete()
    return redirect('studenthome')