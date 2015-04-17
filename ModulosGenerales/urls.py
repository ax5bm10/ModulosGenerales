from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from rest_framework.urls import template_name

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ModulosGenerales.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('API.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    #apis propias
    url(r'^api/', include('API.urls')),
)
