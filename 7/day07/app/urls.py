from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^app/', include('app.urls',namespace='app')),
]
