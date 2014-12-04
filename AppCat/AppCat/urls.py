from django.conf.urls import patterns, include, url
from django.contrib import admin
from AppCat import settings

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'AppCat.views.home', name='home'),
    url(r'^About/$', 'AppCat.views.about', name='about'),
    url(r'^FAQ/$', 'AppCat.views.faq', name='faq'),
    url(r'^login/$', 'AppCat.views.login_user', name='login'),
    url(r'^logout/$', 'AppCat.views.logout_user', name='logout'),
    url(r'^signup/$', 'AppCat.views.signup', name='signup'),
    url(r'^search/$', 'AppCat.views.search', name='search'),
    url(r'^approve/$', 'AppCat.views.approve', name='approve'),
    url(r'^approve/(?P<app_id>\d+)/(?P<choice>[01])$', 'AppCat.views.update_approval', name='update_approval'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^Applications/', include('Applications.urls')),
)

if not settings.DEBUG:
    urlpatterns +=patterns(
        '',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )