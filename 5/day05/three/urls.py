from django.conf.urls import url
from three import views


urlpatterns = [
    url(r'^getdata/$',views.getdata),
    # url(r'^getdata/$',views.getdata),
]
