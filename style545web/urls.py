from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'style545web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
(r'^$', TemplateView.as_view(template_name='static/home/Contact.htm')),
    url(r'^style545app/', include('style545app.urls')),
)
