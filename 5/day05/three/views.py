from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def getdata(request):
    # num = "dd' or '1"  #sql注入
    num = "tom"
    # sql = "select name,age,sex from three_child where name='%s'" % num
    # print(sql)
    with connection.cursor() as cursor:
        # 防止sql注入
        cursor.execute("select name,age,sex from three_child where name=%s",[num])

        # 这种写法无法防止sql注入
        # cursor.execute(sql)
        # data = cursor.fetchall()
        # print(data)

        # 返回列表套字典
        columns = [col[0] for col in cursor.description]
        res = [dict(zip(columns, row)) for row in cursor.fetchall()]
        print(res)
    return HttpResponse("原生sql查询")