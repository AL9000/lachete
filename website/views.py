from django.views import generic
from sondages.models import Question
from blog.models import Article


class HomeView(generic.ListView):
    model = Question
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['last_question'] = Question.objects.filter(
            open=True
        ).latest('pub_date')
        context['last_article'] = Article.objects.filter(
            ouvert=True
        ).latest('date_de_parution')
        return context