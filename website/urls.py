from django.conf.urls import patterns, url
from website.views import HomeView
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import permission_required

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^register/',
        CreateView.as_view(template_name='registration/register.html',
                           form_class=UserCreationForm,
                           success_url='/'),
        name='register'),
    url(r'^organisation/', permission_required('is_staff')(TemplateView.as_view(template_name='website/sheets.html'), ),
        name='organisation'),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login',),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
)
