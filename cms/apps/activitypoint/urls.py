"""cms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.student_activity_view,name='home'),
    path('view/<int:subid>/<int:clasid>/',views.activity_list_view,name='view'),
    path('update_points/<int:pk>/<int:subid>/<int:clasid>/',views.update_points,name="update_points"),
    path('studenthome/',views.student_home_view,name="studenthome"),
    path('deletepoints/<int:pk>/',views.delete_point,name="deletepoints"),

]

