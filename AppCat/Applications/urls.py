from django.conf.urls import patterns, url

from Applications import views

urlpatterns = patterns('',
    # ex: /Applications/  
    url(r'^$', views.index, name='index'),
    # ex: /Applications/5/                                                                                                                                                       
    url(r'^(?P<app_id>\d+)/$', views.detail, name='detail'),
    # ex: /Applications/5/reviews/ 
    url(r'^(?P<app_id>\d+)/reviews/$', views.reviews, name='reviews'),
)
