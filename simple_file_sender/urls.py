from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^simple_file_sender/', include('simple_file_sender.foo.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^upload/$', 'simple_file_sender.views.upload'),
    url(r'^$', 'simple_file_sender.views.index'),
)
