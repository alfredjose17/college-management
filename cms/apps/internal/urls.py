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
    #path('tclass/',views.tclass),
    path('tmarks/<int:subid>/<int:clasid>/',views.entermark,name="marks_enter"),
    path('sview/',views.viewmarks),
    path('tmarks/<int:subid>/<int:clasid>/ascreate/',views.tassignment),
    path('sview/assignview/',views.studassignview,name="studassignment_view"),
    path('sview/assignview/studassignsub/<int:aid>/',views.studassignsubmit),
    path('tmarks/<int:subid>/<int:clasid>/tassignview/',views.tassignview),
]
