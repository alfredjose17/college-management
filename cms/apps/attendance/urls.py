
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('tattendance/<int:subid>/<int:clasid>/',views.enterattendance),
    path('sattendance/',views.viewattendance),

]
