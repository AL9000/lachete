from django.views import generic
from sondages.models import Question
from blog.models import Article


class HomeView(generic.ListView):
    model = Question
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['last_question'] = Question.objects.last()
        context['last_article'] = Article.objects.last()
        return context