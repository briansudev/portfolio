from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'website.views.index', name='index'),
    url(r'^me/$', 'website.views.me', name='me'),
    url(r'^work/$', 'website.views.work', name='me'),
)


