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
            return redirect('home')
    else:
        form=ActivityForm()
    context={
        'form':form
    }
    return render(request,'home.html',context)
def activity_list_view(request):
    queryset=Activitypoint.objects.filter(status="pending")
    context={
        'object_list':queryset
    }
    return render(request,'view.html',context)
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
    queryset=Activitypoint.objects.filter(student__first_name="rrr")    
    context={
        'object':queryset
    }
    return render(request,'studenthome.html',context)
def delete_point(request,pk):
    if request.method=="POST":
        dele=Activitypoint.objects.get(id=pk)
        dele.delete()
    return redirect('studenthome')