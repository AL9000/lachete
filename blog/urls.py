from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from blog import views, feeds


urlpatterns = patterns('',
    url(r'^$', login_required(views.IndexView.as_view()), name='index'),
    url(r'^categorie/(?P<categorie>\S+)$', login_required(views.CategorieView.as_view()), name='categorie'),
    url(r'^(?P<slug>\S+)/$', login_required(views.DetailView.as_view()), name='detail'),
    url(r'^(?P<slug>\S+)/commenter$', login_required(views.CommentaireCreate.as_view()), name='commenter'),

    # TODO Le feed RSS ne fonctionne pas :(
    url(r'^feed/$', login_required(feeds.DerniersArticles()), name='feed'),
)
