from django.shortcuts import  render
from django.shortcuts import  redirect
#from class_project import models
from app01 import models

def get_students(request):
    row_list= models.Student.objects.all()
    '''
    for row in row_list:
        print(row.id,row.username,row.cs.title,row.cs.id)
    '''
    return render(request,'get_students.html',{'row_list ': row_list })

def add_students(request):
    if request.method == 'GET':
        cs_list = models.Classses.objects.all()
        #for row in cs_list:
        #   print(row.id,row.title)
        return render(request,'add_students.html',{'cs_list':cs_list})
    elif request.method == 'POST':
        print(request.POST)
        u = request.POST.get('username')
        a = request.POST.get('age')
        g = request.POST.get('gender')
        c = request.POST.get('cs')
        print(u,a,g,c)
        models.Student.objects.create(
            username= u,
            age=a,
            gender=g,
            cs_id =c
        )
        return redirect('/get_students.html')

def del_students(request):
    nid =request.GET.get('nid')
    models.Student.objects.filter(id=nid).delete()
    return redirect('/get_students.html')

def edit_students(request):
    return redirect('/get_students.html')
