from django.conf.urls import url
from two import views


urlpatterns = [
    url(r'^addteam/$', views.addteam),
    url(r'^addgroup/$',views.addgroup),
    url(r'^deleteteam/$', views.deleteteam),
    url(r'^findgroup/$', views.findgroup),
    url(r'^findteam/$', views.findteam),
    url(r'^lookup/$', views.lookup),

    # 多对多
    url(r'^addproject/$',views.addproject),
    url(r'^querygroup/$', views.querygroup),
    # url(r'^addstudent/$', views.addstudent),
]
