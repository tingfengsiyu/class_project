"""class_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import url
from app01.views import classes
from app01.views import students
from app01.views import get2
from app01.views import ajax

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^classes.html$', classes.get_classesss),
    url(r'^add_classes.html$', classes.add_classes),
    url(r'^del_classes.html$', classes.del_classes),
    url(r'^edit_classes.html$', classes.edit_classes),
    #url(r'^get_students.html$', students.get_studentssss),
    url(r'^add_students.html$', get2.add_students),
    url(r'^del_students.html$', get2.del_students),
    url(r'^edit_students.html$', get2.edit_students),
    url(r'^get.html$',get2.students),
    url(r'^set_teacher.html$',classes.set_teacher),
    url(r'^ajax_students.html$', ajax.edit_students),
    url(r'^ajax2.html$', ajax.ajax2),
    url(r'^ajax3.html$', ajax.ajax3),
]
