from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from website.views import HomeView

urlpatterns = patterns('',
    url(r'^$', login_required(HomeView.as_view()), name="home"),
)
