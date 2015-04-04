from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from photos.views import PhotoCreate

urlpatterns = patterns('',
    url(r'^$', login_required(PhotoCreate.as_view()), name='photo_add'),
)
