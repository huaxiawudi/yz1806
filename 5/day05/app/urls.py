from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^addstudent/$',views.addstudent),
    url(r'^addarchive/$',views.addarchive),
    url(r'^deletestudent/$', views.deletestudent),
    url(r'^getarchive/$', views.get_archive_by_stuent),
    url(r'^getstudent/$', views.getstudent),
    url(r'^lookup/$', views.loopup)

]
