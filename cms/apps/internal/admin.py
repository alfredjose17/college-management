from django.contrib import admin
from .models import  Mark,Internal,TeacherAssignment,StudentAssignment

# Register your models here.
admin.site.register(Mark)
admin.site.register(Internal)
admin.site.register(TeacherAssignment)
admin.site.register(StudentAssignment)