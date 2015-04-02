from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from blog import views


urlpatterns = patterns('',
    url(r'^$', login_required(views.IndexView.as_view()), name='index'),
    url(r'^(?P<pk>\d+)/$', login_required(views.DetailView.as_view()), name='detail'),
)
