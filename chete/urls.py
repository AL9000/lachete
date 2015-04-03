from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^', include('website.urls', namespace="website")),

    url(r'^gps/', include('gps.urls', namespace="gps")),
    url(r'^sondages/', include('sondages.urls', namespace="sondages")),
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^photos/', include('photos.urls', namespace="photos")),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^markdown/', include('django_markdown.urls')),
)
