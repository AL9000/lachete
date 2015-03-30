from django.contrib import admin
from blog.models import Article, Categorie


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,      {'fields': ['titre', 'contenu', 'categorie']}),
        ('Information date', {'fields': ['date_de_parution'], 'classes': ['collapse']}),
    ]
    list_display = ('titre', 'contenu', 'date_de_parution', 'categorie')
    list_filter = ['date_de_parution']
    search_fields = ['titre']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Categorie)