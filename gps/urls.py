from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from gps.views import GPSView
from gps.views import UsersPosition

urlpatterns = patterns('',
    url(r'^users/$', login_required(UsersPosition.as_view()), name='users'),
    url(r'^$', login_required(GPSView.as_view()), name="index"),
)
