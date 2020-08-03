from django.shortcuts import render,redirect,get_object_or_404
from apps.internal.models import Internal

# Create your views here.
    
def home(request):
    if request.user.type == 'teacher':
        if request.method == "POST":
            name = request.POST["class"] 
            classx = get_object_or_404(Internal, teacher = request.user, class_room__name = name)
            #print(classx.class_room.id, classx.subject.id)
            context = {
                'classes' : Internal.objects.filter(teacher = request.user),
                'selected' : classx.class_room,
                'type' : request.user.type,
                'clasid' : classx.class_room.id,
                'subid' : classx.subject.id
            }
        else:
            context = {
                'classes' : Internal.objects.filter(teacher = request.user),
                'type' : request.user.type
            }
    else:
        context = {
            'type' : request.user.type
        }

    return render(request, 'home/index.html', context)
    

def student_profile(request):
    return render(request, 'home/profile.html', {})
