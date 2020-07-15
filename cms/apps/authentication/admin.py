from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from .models import User,Subject,ClassName

from .forms import CustomUserCreationForm , CustomUserChangeForm
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['username', 'email','type','rollno','class_name']
    fieldsets = UserAdmin.fieldsets + (
                         (None, {'fields': ('type','rollno','class_name')}),
                         )

admin.site.register(User, CustomUserAdmin)
admin.site.register(Subject)
admin.site.register(ClassName)
