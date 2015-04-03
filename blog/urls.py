from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from blog import views, feeds


urlpatterns = patterns('',
    url(r'^$', login_required(views.IndexView.as_view()), name='index'),
    url(r'^(?P<slug>\S+)$', login_required(views.DetailView.as_view()), name='detail'),
    # TODO Le feed RSS ne fonctionne pas :(
    url(r'^feed/$', login_required(feeds.DerniersArticles()), name='feed'),
)
