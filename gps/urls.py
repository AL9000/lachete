from django.conf.urls import patterns, url
from gps.views import GPSView

urlpatterns = patterns('',
    url(r'^$', GPSView.as_view(), name="gps"),
)
