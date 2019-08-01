from django.shortcuts import  render
from django.shortcuts import  redirect
# from class_project import models
from app01 import models
def get_classes(request):
    cls_list = models.Classses.objects.all()
    return render(request,'get_classes.html',{'cls_list': cls_list})

def add_classes(request):
    print(request.POST.get('title'))
    if request.method == "GET":
        return render(request,'add_classes.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        models.Classses.objects.create(title=title)
        return redirect('/classes.html')

def del_classes(request):
    nid =request.GET.get('nid')
    models.Classses.objects.filter(id=nid).delete()
    return redirect('/classes.html')

def edit_classes(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        obj = models.Classses.objects.filter(id=nid).first()

        return render(request,'edit_classes.html',{'obj':obj})
    elif request.method == 'POST':
        print(request.POST)
        nid = request.GET.get('nid')
        title = request.POST.get('title')
        models.Classses.objects.filter(id=nid).update(title=title)
        return redirect('/classes.html')
