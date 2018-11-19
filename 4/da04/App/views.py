from random import randint

from django.db.models import Max, Min, Avg, Count, Sum, Q, F
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import Student, Course


def addstudent(request):
    student = Student()
    student.sno = '1806' + str(randint(1,10000))
    student.sname = '栋梁' + str(randint(1,1000))
    student.ssex = '男' if randint(1,2) % 2 else '女'
    student.sclass = '1806'
    student.save()

    return HttpResponse("创建一个学生成功%d" % student.id)

# 返回单个对象的查询
def getoneobject(req):
    # 1. get()只能获取一个对象，
    # stu = Student.objects.get(pk=1)
    # 返回多个对象，会报MultipleObjectsReturned
    # stu = Student.objects.get(sage=0)
    # 不会返回值，会报DoesNotExist
    # stu = Student.objects.get(sage=10)
    # try:
    #     stu = Student.objects.get(sage=10)
    # except Exception as e:
    #     print(e)
    #     return  HttpResponse("学生信息不存在")
    # print(stu)
    # return HttpResponse(stu.sname)

    # 2 first()获取第一个记录
    #   last()获取最后一条记录
    # stu = Student.objects.first()
    # return HttpResponse(stu.sno + "  " + stu.sname)

    # 3 count()获取记录个数
    # res = Student.objects.count()
    # res = Student.objects.filter(sage=0).count()
    # return  HttpResponse("共有：%d" % res)

    # 4 exists()判断查询集中有没有记录，如果有记录返回True，否则返回False
    res = Student.objects.exists()
    if res:
        return HttpResponse("有记录")
    else:
        return HttpResponse("空记录")

# 限制结果集  支持返回查询集的过滤器
def limitset(req):
    # 切片 不支持负索引  返回的是一个集合
    # select * from student limit 2
    # stus = Student.objects.all()[0:2]
    # 隔两条取一条
    # stus = Student.objects.all()[::2]
    # return render(req, 'student.html', context={'data': stus})

    # 索引  返回的是一个对象
    stus = Student.objects.all()[3]
    return render(req,'student.html', context={'data':[stus]})

def fieldquery(req):
    # 1 iexact 不区分大小写精确匹配
    # stu = Student.objects.filter(sname__iexact='admin')

    # 2 icontains 包含，相当于 like '%data%'
    # stu = Student.objects.filter(sname__icontains='栋梁')

    # 3 startwith 以...开头
    # stu = Student.objects.filter(sname__startswith='A')

    # 4 isnull  判字段是否为空
    # select *from student where sage is null
    # stu = Student.objects.filter(sage__isnull=True)

    # 5 关于运算
    # select * from student where id>2 and i<6
    # stu = Student.objects.filter(id__gt=2,id__lt=6)

    # 6 in 集合运算
    # stu = Student.objects.filter(id__in=[1,4,6])
    # stu = Student.objects.filter(id__in=(1,4,6))
    # in后可以跟子查询，但子查询只能返回一个字段
    # sub = Student.objects.filter(id__lte=5).values('id')
    # stu = Student.objects.filter(id__in=sub)

    # 7 regex 正则
    # python支持utf8，python正则规则中 \d不表示纯数字，要表示纯数字应该用[0-9]
    stu = Student.objects.filter(sname__regex=r'[0-9]+$')
    print(stu.query)
    return render(req,'student.html',context={'data':stu})


# 统计
def groupby(request):
    # 统计Max、Min、Count、Sum、Avg
    # select max(id),min(id),avg(id) from student
    # maxid = Student.objects.aggregate(Max('id'))
    # minid = Student.objects.aggregate(Min('id'))  # {'id__min': 1}
    # avgid = Student.objects.aggregate(Avg('id'))
    # return HttpResponse("max={} min={} avg={}".format(maxid, minid, avgid))

    # 分组统计  返回的是QuerySet
    # 使用values进行分组，使用annotate统计
    # res = Student.objects.values('ssex').annotate(Count('id'))
    res = Student.objects.values('sclass','ssex').annotate(Count('id'))
    print(res.query)

    return HttpResponse(res)

# Q对象和F对象
def QandF(req):
    # 逻辑或 |
    # select * from student where uid=2 or uid = 3
    # stu = Student.objects.filter(Q(id=2) | Q(id=5))
    # 逻辑与 &
    # stu = Student.objects.filter(Q(id__gte=2) & Q(id__lte=5))
    # 逻辑取反 ~
    # stu = Student.objects.filter(~Q(id__gte=2))

    # F对象，表示表中两列的对比
    stu = Student.objects.filter(sage__gt=F('id'))
    # print(stu)
    return render(req,'student.html', context={'data':stu})



# 自定义管理器
def addcourse(req):
    # course = Course(cname='python从入门到精通%d' % randint(1,100) , ccredit=4)
    # course.save()
    # 用自定义管理器对象创建新对象
    course = Course.gmanager.create('计算机组成原理', 4.5)
    return HttpResponse("增加一门新课程%d" % course.id)

def getcourse(req):
    # 一旦自定义管理器对象后，就不能再使用objects
    # course = Course.objects.all()
    course = Course.cmanager.all()
    print(course.values('cname').count())
    course = Course.gmanager.all()
    print(course.values('cname').count())
    return HttpResponse("获取课程")