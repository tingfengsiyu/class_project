from django.shortcuts import  render
from django.shortcuts import  redirect
from class_project import models


def get_students(request):
    stu_list= models.Student.objects.all()
    for row in stu_list:
        print(row.id,row.username,row.cs.title,row.cs.id)
    return render(request,'get_studentes.html',{'stu_list ':stu_list})

def add_students(request):
    if request.method == 'GET':
        cs_list = models.Classes.objects.all()
        #for row in cs_list:
        #   print(row.id,row.title)
        return render(request,'add_students.html',{'cs_list':cs_list})
    elif request.method == 'POST':
        u = request.POST.get('username')
        a = request.POST.get('age')
        g = request.POST.get('gender')
        c = request.POST.get('cs')
        print(u,a,g,c)
        models.Students.objects.create(
            username= u,
            age=a,
            gender=g,
            cs_id =c

        )
        return  redirect('/students.html')

def del_students(request):
    nid =request.GET.get('nid')
    models.Student.objects.filter(id=nid.delete())
#
    return redirect('/students.html')

