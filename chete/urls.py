from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^gps/$', include('gps.urls', namespace="gps")),
    url(r'^sondages/', include('sondages.urls', namespace="sondages")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('website.urls', namespace="website")),
)
