from django.conf.urls import url
from four import views


urlpatterns = [
    url(r'^hello/(\w+)/$',views.hello),
    url(r'^hello/(\w+)/(\d+)/$',views.hello2),
]
