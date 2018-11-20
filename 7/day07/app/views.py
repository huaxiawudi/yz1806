from random import randint

from django.shortcuts import render

# Create your views here.
def add_student(request):
    stu = Student()
    stu.sname = '小明' + str(randint(1,1000))
    stu.ssex = randint(0,1)
    stu.sage = randint(15,30)
    stu.save()
    return HttpResponse("添加学生%d" % stu.id)