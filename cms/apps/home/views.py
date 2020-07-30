from django.shortcuts import render,redirect

# Create your views here.

def student_home(request):
    return render(request, 'home/index.html', {})
    
def teacher_home(request):
    return render(request, 'home/index-teacher.html', {})

def student_profile(request):
    return render(request, 'home/profile.html', {})
