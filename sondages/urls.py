from django.conf.urls import patterns, url

from sondages import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/resultats/$', views.ResultsView.as_view(), name='resultats'),
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)