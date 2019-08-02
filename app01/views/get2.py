from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from app01 import models


def students(request):
    cls = models.Student.objects.all()
    for row in cls:
        print(row.id, row.username, row.age)
    # return HttpResponse('1112')
    return render(request, 'get_stu.html', {'cls': cls})

def add_students(request):
    if request.method == 'GET':
        cs_list = models.Student.objects.all()
        for row in cs_list:
            print(row.username,row.age,row.gender,row.cs.id,row.cs.title)
        return render(request, 'add_students.html', {'cs_list': cs_list})
    elif request.method == 'POST':
        print(request.POST)
        u = request.POST.get('username')
        a = request.POST.get('age')
        g = request.POST.get('gender')
        c = request.POST.get('cs')
        print(u, a, g, c)
        models.Student.objects.create(
            username=u,
            age=a,
            gender=g,
            cs_id=c
        )
        return redirect('/get.html')


def del_students(request):
    nid = request.GET.get('nid')
    models.Student.objects.filter(id=nid).delete()
    return redirect('/get.html')


def edit_students(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        obj = models.Student.objects.filter(id=nid).first()
        return render(request,'edit_students.html',{'obj':obj})
    elif request.method == 'POST':
        print(request.POST)
        nid = request.GET.get('nid')
        username = request.POST.get('username')
        age = request.POST.get('age')
        models.Student.objects.filter(id=nid).update(username=username)
        models.Student.objects.filter(id=nid).update(age=age)
        return redirect('/get.html')