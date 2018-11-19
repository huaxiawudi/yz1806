from django.shortcuts import render, HttpResponse

# Create your views here.
# 视图函数必须有一个参数，参数是用户的请求对象，由django传递
from firstday.models import User


def index(req):
    # HttpResponse 返回给客户端的信息，可以是html、json、xml、或者重定向
    # 最简单用法是返回一个字符串给客户端
    # return HttpResponse("大家好！，这是我的第一个网站")

    # render是HtttpResponse的简写,负责渲染模板
    # return render(req, 'index.html')

    # 模板带变量
    data = ['张飞','岳飞','关公','秦琼']
    return render(req, 'index.html',context={'content':"---莫言",'data':data})

# 用户列表
def listuser(req):
    # 获取用户表中所有的数据
    res = User.objects.all()
    return render(req, 'userlist.html',context={'data':res})
