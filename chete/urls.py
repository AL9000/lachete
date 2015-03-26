from django.conf.urls import patterns, include, url
from django.contrib import admin
from chete.views import HomeView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^sondages/', include('sondages.urls', namespace="sondages")),
    url(r'^admin/', include(admin.site.urls)),
)
