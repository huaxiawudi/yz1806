from random import randint

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from two.models import Team, Group1, Project


def addteam(request):
    team = Team(tname=str(randint(1801,1807)))
    team.save()
    return HttpResponse("增加班级")

#
def addgroup(request):
    g1 = Group1(gname='起的隆冬强%d' % randint(1,100))
    g1.team = Team.objects.first()
    g1.save()
    return HttpResponse("增加小组")

# 删除班级
def deleteteam(req):
    # 外键设置为DO_NOTHING，从表中有记录依赖主表记录，则主表记录不允许删除
    team = Team.objects.first()
    team.delete()
    return HttpResponse("删除班级")

# 正向查询
def findgroup(req):
    t1 = Team.objects.last()
    # 主表对象.从表_set.过滤器方法
    print(t1.group1_set.all())
    return HttpResponse("获取指定班级的组")

# 方向查询
def findteam(req):
    g1 = Group1.objects.last()
    # 一个组对应一个班级，可以通过team直接获取班级信息
    print(g1.team.tname)
    return HttpResponse("通过组获取班级信息")

def lookup(req):
    # team = Team.objects.filter(group1__id=5)
    g1 = Group1.objects.filter(team__tname='1804')
    return HttpResponse(g1)

# ------------------------------------------------------
# 多对多
def addproject(req):
    p1 = Project(pname='我的博客')
    p1.save()  #项目必须在数据库中存在
    g1 = Group1.objects.get(pk=2) # 组必须在数据库中存在
    g2 = Group1.objects.get(pk=4)

    # 指定项目的组  添加到project_group1表中
    p1.group1.add(g1,g2)

    return HttpResponse("创建项目")

# 正向查询
def querygroup(req):
    # 反向查询
    # 获取项目
    # p1 = Project.objects.get(pk=1)
    # 通过项目获取组的信息
    # g1 = p1.group1.all()

    # 正向查询
    # 组信息
    g2 = Group1.objects.get(pk=2)
    # 带_set的是从表
    project = g2.project_set.all()
    return  HttpResponse(project)
