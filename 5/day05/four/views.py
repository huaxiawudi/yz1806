from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request,num1):

    return HttpResponse("{}".format(num1))


def hello2(request,*args):
    print(args)
    for x in request.GET.lists():
        print(x)
    return HttpResponse("任意位置参数")