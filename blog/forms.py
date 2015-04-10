from django.forms import ModelForm
from blog.models import Commentaire


class CommentaireForm(ModelForm):
    class Meta:
        model = Commentaire
        fields = ['titre', 'contenu']