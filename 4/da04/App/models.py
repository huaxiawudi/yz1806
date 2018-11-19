from django.db import models


# 自定义管理器类
class MyManager(models.Manager):
    def get_queryset(self):
        # 只返回没有逻辑删除的数据
        return super().get_queryset().filter(is_deleted=False)

    # 扩展新功能
    def create(self,cname,ccredit):
        course = Course()
        course.cname = cname
        course.ccredit = ccredit
        course.save()
        return course


# Create your models here.
class Student(models.Model):
    sno = models.CharField(max_length=10,unique=True)
    sname = models.CharField(max_length=50,null=True)
    ssex = models.CharField(max_length=2,default='男')
    sage = models.IntegerField(null=True,default=0)
    sclass = models.CharField(max_length=5)

    def __str__(self):
        return "学号：{},姓名：{}".format(self.sno,self.sname)

    class Meta:
        db_table = 'student'

class Course(models.Model):
    cname = models.CharField(max_length=30)
    ccredit = models.FloatField(null=True)
    is_deleted = models.NullBooleanField(default=False,null=True)


    # 自定义管理器对象，原来objects不能再用
    cmanager = models.Manager()

    # 自定义管理器的对象
    gmanager = MyManager()

    def __str__(self):
        return self.cname