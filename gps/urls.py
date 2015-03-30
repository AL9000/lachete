from django.conf.urls import patterns, url
from gps.views import GPSView
from gps.views import UsersPosition

urlpatterns = patterns('',
    url(r'^users/$', UsersPosition.as_view(), name='users'),
    url(r'^$', GPSView.as_view(), name="index"),
)
