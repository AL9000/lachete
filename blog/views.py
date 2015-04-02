from blog.models import Article, Categorie
from django.views import generic


class IndexView(generic.ListView):
    queryset = Article.objects.published()
    model = Article
    template_name = 'blog/index.html'
    paginate_by = 2


class DetailView(generic.DetailView):
    model = Article
    template_name = 'blog/article.html'