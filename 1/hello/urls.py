import views
urlpatterns = ((r'^/$', views.index),
        (r'^/login/$', views.login),
        (r'^/register/$',views.register)
        )
