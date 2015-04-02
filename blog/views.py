from blog.models import Article
from django.views import generic


class IndexView(generic.ListView):
    queryset = Article.objects.published()
    model = Article
    template_name = 'blog/index.html'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['derniers_articles'] = Article.objects.all()
        return context


class DetailView(generic.DetailView):
    model = Article
    template_name = 'blog/article.html'