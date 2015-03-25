import datetime

from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse

from sondages.models import Question


class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently doit retourner false pour les questions avec une pub_date future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() doit retourner false pour les questions ayant leur pub_date de plus d'un jour.
        """
        time = timezone.now() - datetime.timedelta(days=30)
        old_question = Question(pub_date=time)
        self.assertEqual(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() doit retourner True pour les questions qui ont leur pub_date à moins d'un jour.
        """
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date=time)
        self.assertEqual(recent_question.was_published_recently(), True)


def create_question(question_text, days):
    """
    Créé une question avec 'question_text' publiée le nombre de jours 'days' à partir de maintenant (nombre de jours
    négatifs pour une question publiée dans le passé, et positifs pour une question à publier).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionViewTests(TestCase):
    def test_index_view_with_no_questions(self):
        """
        Si il n'y a pas de questions, un message le signalant doit être affiché.
        """
        response = self.client.get(reverse('sondages:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Aucuns sondages disponibles.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_index_view_with_a_past_question(self):
        """
        Questions with a pub_date in the past should be displayed on the
        index page.
        """
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('sondages:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_index_view_with_a_future_question(self):
        """
        Questions with a pub_date in the future should not be displayed on
        the index page.
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('sondages:index'))
        self.assertContains(response, "Aucuns sondages disponibles.",
                            status_code=200)
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_index_view_with_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        should be displayed.
        """
        create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('sondages:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_index_view_with_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('sondages:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )


class QuestionIndexDetailTests(TestCase):
    def test_detail_view_with_a_futur_question(self):
        """
        La vue détaillée d'une question qui n'est pas encore publiée doit retourner une erreur 404.
        """
        futur_question = create_question(question_text="Future question.", days=5)
        response = self.client.get(reverse('sondages:detail', args=(futur_question.id,)))
        self.assertEqual(response.status_code, 404)

    def test_detail_view_with_a_past_question(self):
        """
        La vue détaillée d'une question déjà publiée doit afficher le texte de la question.
        """
        past_question = create_question(question_text='Past question.', days=-5)
        response = self.client.get(reverse('sondages:detail', args=(past_question.id,)))
        self.assertContains(response, past_question.question_text, status_code=200)


class QuestionResultsTests(TestCase):
    def test_results_view_with_a_futur_question(self):
        """
        Les résultats d'une question qui n'est pas encore publiée doit retourner une erreur 404.
        """
        futur_question = create_question(question_text="Future question.", days=5)
        response = self.client.get(reverse('sondages:resultats', args=(futur_question.id,)))
        self.assertEqual(response.status_code, 404)

    def test_results_view_with_a_past_question(self):
        """
        Les résultats d'une question déjà publiée doit afficher la page des résultats.
        """
        past_question = create_question(question_text='Past question.', days=-5)
        response = self.client.get(reverse('sondages:resultats', args=(past_question.id,)))
        self.assertContains(response, past_question.question_text, status_code=200)