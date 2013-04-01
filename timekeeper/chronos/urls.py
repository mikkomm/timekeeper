from django.conf.urls import patterns, url
from chronos import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<project_id>\d+)/project/$', views.project, name='project'),
    url(r'^(?P<task_id>\d+)/task/$', views.task, name='task'),
    url(r'^(?P<reference_id>\d+)/reference/$', views.reference, name='reference'),
)
