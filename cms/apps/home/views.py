from django.shortcuts import render,redirect,get_object_or_404
from apps.internal.models import Internal
from django.http import HttpResponse

# Create your views here.
    
def home(request):
    if request.user.type == 'teacher':
        if request.method == "POST":
            name = request.POST["class"] 
            classx = get_object_or_404(Internal, teacher = request.user, class_room__name = name)
            context = {
                'classes' : Internal.objects.filter(teacher = request.user),
                'selected' : classx.class_room,
                'type' : request.user.type,
                'clasid' : classx.class_room.id,
                'subid' : classx.subject.id,
                'classname' : request.user.class_name,
                'fname' : request.user.first_name,
                'lname' : request.user.last_name,
                'roll' : request.user.rollno,
            }

        else:
            context = {
                'classes' : Internal.objects.filter(teacher = request.user),
                'selected' : get_object_or_404(Internal, class_room__id = 1).class_room,
                'clasid' : get_object_or_404(Internal, class_room__id = 1).class_room.id,
                'subid' : get_object_or_404(Internal, class_room__id = 1).subject.id,
                'type' : request.user.type,
                'classname' : request.user.class_name,
                'fname' : request.user.first_name,
                'lname' : request.user.last_name,
                'roll' : request.user.rollno,
            }
    else:
        context = {
            'type' : request.user.type,
            'fname' : request.user.first_name,
            'lname' : request.user.last_name,
            'classname' : request.user.class_name,
            'roll' : request.user.rollno,
        }
    print(context)
    return render(request, 'home/index.html', context)
    

def student_profile(request):
    return render(request, 'home/profile.html', {})
