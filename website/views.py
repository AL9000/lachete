from django.views import generic
from sondages.models import Question
from blog.models import Article
from django.utils import timezone


class HomeView(generic.ListView):
    model = Question
    template_name = "website/templates/website/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        if Question.objects.filter(open=True):
            context['last_question'] = Question.objects.filter(
                open=True,
                pub_date__lte=timezone.now(),
            ).latest('pub_date')
        context['last_article'] = Article.objects.filter(
            ouvert=True
        ).latest('date_de_parution')
        return context