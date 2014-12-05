from django.conf.urls import patterns, url

from Applications import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<app_id>\d+)/$', views.detail, name='detail'),
    url(r'^add_review/(?P<app_id>\d+)/', views.add_review, name='add'),
    url(r'^submit/', views.submit, name='submit'),

    
)
