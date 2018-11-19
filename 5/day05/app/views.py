from random import randint

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from app.models import Student, Archive


# 增加学生
def addstudent(request):
    list1 = ['张','李','赵','顾','夏']
    list2 = ['雪','峰','军','国','辉']
    student = Student()
    student.sname = list1[randint(0,4)] + list2[randint(0,4)]
    student.save()
    return HttpResponse("增加学生%d" % student.id)

# 增加档案
def addarchive(req):
    archive = Archive()
    archive.phone = str(randint(100000000,1000000000))
    # student 必须是数据库中有的学生
    archive.student = Student.objects.get(pk=randint(1,Student.objects.count()))
    archive.save()
    return  HttpResponse("增加学生档案%d" % archive.id)

# 删除学生
def deletestudent(req):
    try:
        student = Student.objects.get(pk=5)
        student.delete()
    except Exception as e:
        print(e)
        return HttpResponse("学生不存在")

    return  HttpResponse("删除学生")

# 正向查询 由主表查从表
def get_archive_by_stuent(req):
    student = Student.objects.get(pk=8)
    print(student)
    # 查学生的档案
    print(student.archive)  #从表是类名的小写
    return HttpResponse("查看学生档案")
# 反向查询  由从表查主表
def getstudent(req):
    archive = Archive.objects.get(pk=1)
    print(archive)
    print(archive.student) #主表名是类名的小写
    return HttpResponse("由档案查看学生信息")

# 夸关系查询
def loopup(req):
    # 根据学生查档案
    archive = Archive.objects.filter(student__sname='夏峰')

    # 由档案查学生
    # student = Student.objects.filter(archive__phone='351654555')
    return HttpResponse(archive)