from django.contrib import admin
from blog.models import Article, Categorie
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField


class ArticleAdmin(MarkdownModelAdmin):
    prepopulated_fields = {'slug': ('titre',)}
    list_display = ('titre', 'contenu', 'categorie')
    list_filter = ['date_de_parution']
    search_fields = ['titre']
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}


admin.site.register(Article, ArticleAdmin)
admin.site.register(Categorie)