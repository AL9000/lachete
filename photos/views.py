from django.views.generic.edit import CreateView
from photos.models import Photo


class PhotoCreate(CreateView):
    model = Photo
    fields = ['photo']
    template_name = 'photos/index.html'