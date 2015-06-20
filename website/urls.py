from django.conf.urls import patterns, url
from website.views import HomeView
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from website.admin import UserCreationForm
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^register/',
        CreateView.as_view(template_name='registration/register.html',
                           form_class=UserCreationForm,
                           success_url='/'),
        name='register'),
    url(r'^organisation/', staff_member_required(TemplateView.as_view(template_name='website/sheets.html'), ), name='organisation'),


    # Reset password
    url(r'^reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'template_name': 'registration/reset_confirm.html',
         'post_reset_redirect': '/done/'},
        name='reset_confirm'),
    url(r'^reset/$',
        'django.contrib.auth.views.password_reset',
        {'template_name': 'registration/reset.html',
         'email_template_name': 'registration/mails/reset_email.html',
         'subject_template_name': 'registration/mails/reset_subject.txt',
         'post_reset_redirect': '/reset/done/'},
        name='reset'),
    # TODO les templates définis dans registrations ne sont pas pris en compte, pk ?
    url(r'^done/$',
        'django.contrib.auth.views.password_reset_complete',
        name='reset_done'),
    url(r'^reset/done/$',
        'django.contrib.auth.views.password_reset_done'),


    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name="login"),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="logout"),
)
