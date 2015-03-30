from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from sondages.models import Question, Choix


# TODO Paginator !!!
def listing(request):
    question_list = Question.objects.all()
    paginator = Paginator(question_list, 25)  # Show 25 questions per page

    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        questions = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        questions = paginator.page(paginator.num_pages)

    return render_to_response('sondages/detail.html', {"questions": questions})


class IndexView(generic.ListView):
    model = Question
    template_name = 'sondages/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['last_question'] = Question.objects.filter(
            pub_date__lte=timezone.now(),
            open=True
        ).latest('pub_date')
        """ latest_question_list ne contient pas la dernière question posée """
        context['latest_question_list'] = Question.objects.filter(
            pub_date__lte=timezone.now(),
            open=True
        ).order_by('-pub_date')[1:]
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
    # Si la question est close, on redirige vers le résultat du sondage
    if not p.open:
        return HttpResponseRedirect(reverse('sondages:resultats', args=(p.id,)))
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