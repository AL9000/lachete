from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from sondages.views import IndexView, DetailView, ResultsView, vote


urlpatterns = patterns('',
    url(r'^$', login_required(IndexView.as_view()), name='index'),
    url(r'^(?P<slug>\S+)/$', login_required(DetailView.as_view()), name='detail'),
    url(r'^(?P<slug>\S+)/resultats$', login_required(ResultsView.as_view()), name='resultats'),
    url(r'^(?P<slug>\S+)/vote$', login_required(vote), name='vote'),
)
