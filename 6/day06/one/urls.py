
from django.conf.urls import url, include
from one import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addstudent/$',views.add_student,name='addstudent'),
    url(r'^addteam/$', views.add_team,name='addteam'),
    url(r'^teamlist/$', views.list_team,name='teamlist'),

    # 动态url解析
    # 没有命名的组
    url(r'^studentlist/(\d+)/$',views.studentlist,name='studentlist'),
    url(r'^studentlist2/(?P<tid>\d+)/$',views.studentlist2,name='studentlist2'),
    # 命名组
    # url(r'^studentlist/(\w+)/(\d+)/$',views.studentlist,name='studentlist')


    #request对象
    url(r'^req/$',views.requestlist, name='req'),

    # get/post
    url(r'^showregister/$',views.show_register,name='showregister'),
    url(r'^register/$',views.register, name='register'),

    # response
    url(r'^hello/$',views.hello,name='hello'),
    url(r'^json/$',views.processjson,name='json'),

    # 重定向
    url(r'^cdj/(\d+)/$',views.chong,name='cdj'),
    url(r'^cdj2/$',views.chong2,name='cdj2'),
]
