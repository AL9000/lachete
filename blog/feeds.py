from django.contrib.syndication.views import Feed
from blog.models import Article


class DerniersArticles(Feed):
    title = "La Chête"
    link = "/feed/"
    description = "Les dernières niouzes de la Chête"

    def items(self):
        return Article.objects.published()[:5]

    def item_title(self, item):
        return item.titre

    def item_description(self, item):
        return item.contenu


