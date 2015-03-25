from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from sondages.models import Question, Choix


class IndexView(generic.ListView):
    template_name = 'sondages/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Retourne les 5 dernières questions publiées ouvertes au vote (n'inclue pas les questions à publier dans le futur)."""
        return Question.objects.filter(
            pub_date__lte=timezone.now(),
            open=True
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'sondages/detail.html'

    def get_queryset(self):
        """
        Exclu les questions qui ne sont pas encore publiées.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'sondages/resultats.html'

    def get_queryset(self):
        """
        Exclu les questions qui ne sont pas encore publiées.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choix = p.choix_set.get(pk=request.POST['choix'])
    except (KeyError, Choix.DoesNotExist):
        # Réaffiche le formulaire de vote de la question
        return render(request, 'sondages/detail.html', {
            'question': p,
            'error_message': "Vous n'avez pas séléctionné votre choix.",
        })
    else:
        selected_choix.votes += 1
        selected_choix.save()
        return HttpResponseRedirect(reverse('sondages:resultats', args=(p.id,)))