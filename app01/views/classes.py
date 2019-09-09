from django.shortcuts import  render
from django.shortcuts import  redirect
from app01 import models
def get_classesss(request):
    cls_list = models.Classses.objects.all()
    """
    for obj in cls_list:
        '''多对多查询
        将表的id与其他表关联
        自动生成id，班级id，老师id
        1	1	1
        2	1	2

        
        '''
        print(obj.id,obj.title,obj.m.all())
        #1 1班 <QuerySet [<Teachers: Teachers object (1)>, <Teachers: Teachers object (2)>]>
        for row in obj.m.all():
            print('---',row.name)
            '''
            1班 <QuerySet [<Teachers: Teachers object (1)>, <Teachers: Teachers object (2)>]>
            --- luofeng
            --- luofeng1
            '''
    #print(type(cls_list))

    #多对多操作
    #obj=models.Classses.objects.filter(id=1).first()
    #obj.m.add(4)        #在第三张表操作   新增一条 班级id为3

    obj= models.Teachers.objects.filter(id=2).first()
    #obj.classses_set.add(3)     #反向查找，在第三张表里面新建 老师id为3的关联
    #obj.sss.add(2)      #反向查找默认使用set，即表名然后_set，如果在多对多关系创建时，添加了m = models.ManyToManyField("Teachers",related_name='sss')，那么就可以直接使用sss，无需set
    obj.sss.set([1,2])  #该删除的删除，如果有不动，删除  老师id为2，而后  班级id为1和2的之外的
    """
    #v = models.Classses.objects.all().values('id','title','m','m__name')
    v= models.Teachers.objects.all().values('name','sss__student')
    print(v)
    '''
    models.Classses.objects.all().values('id','title')
    <QuerySet [{'id': 1, 'title': '1班'}, {'id': 2, 'title': '2班'}, {'id': 3, 'title': '3班'}]>
    
    models.Classses.objects.all().values('id','title','m')
    < QuerySet[{'id': 1, 'title': '1班', 'm': 1}, {'id': 1, 'title': '1班', 'm': 2}, {'id': 1, 'title': '1班', 'm': 3}, {
        'id': 1, 'title': '1班', 'm': 4}, {'id': 2, 'title': '2班', 'm': 2}, {'id': 3, 'title': '3班', 'm': None}] >
        
    models.Classses.objects.all().values('id','title','m','m__name')    
    <QuerySet [{'id': 1, 'title': '1班', 'm': 1, 'm__name': 'luofeng'}, {'id': 1, 'title': '1班', 'm': 2, 'm__name': 'luofeng1'}
    
    models.Teachers.objects.all().values('name','sss__student')
    {'name': 'luofeng', 'sss__student': 8}, {'name': 'luofeng', 'sss__student': 9}, {'name': 'luofeng1', 'sss__student': 8}
    '''
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
