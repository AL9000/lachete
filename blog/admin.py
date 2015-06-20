from django.contrib import admin
from blog.models import Article, Categorie, Commentaire
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField


class ArticleAdmin(MarkdownModelAdmin):
    list_display = ['titre', 'categories', 'apperçu_du_texte', 'lien_video', 'date_de_parution', 'ouvert']
    list_filter = ['date_de_parution']
    search_fields = ['titre']
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

    def lien_video(self, obj):
        if obj.video:
            return True
        return False
    lien_video.boolean = True

    def apperçu_du_texte(self, obj):
        if len(obj.contenu) > 40:
            return obj.contenu[0:40] + '...'
        return obj.contenu

    def categories(self, obj):
        return ', '.join([str(a) for a in obj.categorie.all()])


class CommentaireAdmin(admin.ModelAdmin):
    list_display = ['utilisateur', 'titre', 'contenu', 'article', 'date_de_parution']
    ordering = ['-date_de_parution']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Categorie)
admin.site.register(Commentaire, CommentaireAdmin)