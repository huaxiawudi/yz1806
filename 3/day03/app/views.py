from django.http import HttpResponse
from django.shortcuts import render
from hashlib import md5  #内置库，md5用于签名
from random import randint

# Create your views here.
# 增加用户
from app.models import User


def adduser(req):
    # 创建一个用户
    user = User()
    user.username = '王思聪' + str(randint(1,10000))
    user.password = md5(b'123').hexdigest()
    user.ip = '128.9.7.1'

    # 保存
    user.save()
    return HttpResponse("添加新用户" + str(user.id))

# 修改用户
def updateuser(req):
    # 获取第一条记录
    user = User.objects.first()

    # 修改一条记录
    # user.username = '隔壁老王'
    # user.save()

    # 修改多条记录
    users = User.objects.all()   #获取所有记录
    users.update(ip='8.8.8.8')

    return HttpResponse("修改成功")

# 删除记录
def deleteuser(req):
    # 获取最后一条记录
    user = User.objects.last()

    # 删除
    res = user.delete()
    print(res)
    return HttpResponse("删除记录")

# 查询
# 返回查询结果集
def getqueryset(req):
    # 1.获取所有数据 all()
    # users = User.objects.all()
    # print(users)
    # print(type(users))
    # 2 数据过滤
    # res = users.filter(username='隔壁老王')
    # res = users.filter()  # 所有记录，没有过滤
    # res = users.filter().filter(password='111')

    # 两个条件之间是逻辑与的关系
    # select * from user where username='隔壁老王' and password='111'
    # res = users.filter(username='隔壁老王', password='111')
    # res = users.filter(username='隔壁老王').filter(password='111')

    # print(res,type(res))
    # return HttpResponse("查询所有数据")

    # 3 exclue 排除满足条件的记录
    # select * from user where not (username='王思聪')
    # res = User.objects.exclude(username='王思聪')
    # print(res)
    # 4 排序 order_by
    # res = User.objects.all().order_by('id')  #升序
    # res = User.objects.all().order_by('-id')  #降序
    # res = User.objects.all().order_by('username','-id')  #多列排序

    # 4 字段过滤 values()
    # res = User.objects.values()  #所有字段
    # res = User.objects.values('username','password')
    # print(res)

    # 5 去重 distinct()
    # res = User.objects.all().values('username').distinct()

    # 6 对排序结果反转 reverse()
    res = User.objects.all().order_by('-id').reverse()

    print(res)
    # return render(req,'userlist.html', context={'data':res})
    return render(req,'fields.html', context={'data':res})
