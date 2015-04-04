from django import forms
from photos.models import Photo


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['photo']