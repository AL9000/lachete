from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from sondages.models import Question, Choix


class IndexView(generic.ListView):
    model = Question
    template_name = 'sondages/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        if Question.objects.all().exists():
            test = Question.objects.filter(
                pub_date__lte=timezone.now(),
                open=True
            ).order_by('-pub_date')
            if test:
                context['last_question'] = test[0]
                """ latest_question_list ne contient pas la dernière question posée """
                context['latest_question_list'] = test[1:]

            context['closed_question_list'] = Question.objects.filter(
                pub_date__lte=timezone.now(),
                open=False
            ).order_by('-pub_date')

        return context


class DetailView(generic.DetailView):
    model = Question
    template_name = 'sondages/detail.html'

    def get_queryset(self):
        """
        Exclu les questions qui ne sont pas encore publiées.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        if self.request.user in self.object.votants.all():
            context['vote'] = True
        else:
            context['vote'] = False
        return context


class ResultsView(DetailView):
    template_name = 'sondages/resultats.html'


def vote(request, slug):
    p = get_object_or_404(Question, slug=slug)
    # Si la question est close, ou si l'utilisateur a déjà voté
    # on redirige vers le résultat du sondage = sécurité suplémentaire
    if (not p.open) or (request.user in p.votants.all()):
        return HttpResponseRedirect(reverse('sondages:resultats', args=(p.slug,)))
    try:
        selected_choix = p.choix_set.get(pk=request.POST['choix'])
    except (KeyError, Choix.DoesNotExist):
        # Réaffiche le formulaire de vote de la question
        return render(request, 'sondages/detail.html', {
            'question': p.slug,
            'error_message': "Vous n'avez pas séléctionné votre choix.",
            })
    else:
        selected_choix.votes += 1
        selected_choix.save()
        p.votants.add(request.user)
        p.save()
        return HttpResponseRedirect(reverse('sondages:resultats', args=(p.slug,)))
