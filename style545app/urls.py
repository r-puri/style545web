from django.conf.urls import patterns, url
from style545app import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^looks', views.index, name='index'),
        url(r'^getitemsbycat', views.getitemsbycat, name='getitemsbycat'),
        url(r'^register', views.register, name='register'),
         url(r'^login', views.user_login, name='login'),
         url(r'^logout', views.user_logout, name='logout'),
         url(r'^lookconfirm', views.lookconfirm, name='lookconfirm'),
         url(r'^viewlook', views.viewlook, name='viewlook'),
         url(r'^updatelook', views.updatelook, name='updatelook'),
         url(r'^survey', views.survey, name='survey'),
         url(r'^showlook', views.surveycomplete, name='surveycomplete'),
         url(r'^createsurvey', views.createsurvey, name='createsurvey'),
         url(r'^createvendor', views.createvendor, name='createvendor'),
         url(r'^instore', views.instore, name='instore'),
         url(r'^storeview', views.instoreview, name='instoreview')




        )
