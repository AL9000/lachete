from django.conf.urls import patterns, url, include
from website.views import HomeView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name="home"),
    # TODO Login after register ?
    url('^register/', CreateView.as_view(
        template_name='registration/register.html',
        form_class=UserCreationForm,
        success_url='/',),
        name='register'),

    # TODO Utiliser le parametre next pour rediriger l'utilisateur à la page souhaitée initialement après le login
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
)
