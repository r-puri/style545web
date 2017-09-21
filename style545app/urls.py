from django.conf.urls import patterns, url
from style545app import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^looks', views.index, name='index'),
        url(r'^getitemsbycat', views.getitemsbycat, name='getitemsbycat'),
        url(r'^register', views.register, name='register'),
         url(r'^login', views.user_login, name='login'),
         url(r'^logout', views.user_logout, name='logout'),
         url(r'^lookconfirm', views.lookconfirm, name='lookconfirm')

        )
