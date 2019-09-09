from django.db import models
# from class_ project import models
#from app01 import models
class Classses(models.Model):
    '''
    班级表
    '''
    title = models.CharField(max_length=32)
    m = models.ManyToManyField("Teachers",related_name='sss')


class Teachers(models.Model):
    '''
    老师表
    '''
    name = models.CharField(max_length=32)


'''
cid_id tid_id
1   1
1   2
6   1
  django 会自动创建相应的多对多关系，只需要声明ManyToManyField即可
class C2T(models.Model):
    cid = models.ForeignKey(Classses)
    tid = models.ForeignKey(Teachers)

'''


class Student(models.Model):
    username = models.CharField(max_length=24)
    age = models.IntegerField()
    gender = models.NullBooleanField()  # 可以为空的布尔值
    cs = models.ForeignKey(Classses,on_delete=models.CASCADE)
    #django 2.0 与django1.0不同的是，django1.0不需要添加on_delete，django2.0需要添加on_delete

