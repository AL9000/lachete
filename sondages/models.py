import datetime
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


class QuestionQuerySet(models.QuerySet):
    def published(self):
        return self.filter(open=True, pub_date__lte=timezone.now())


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    pub_date = models.DateTimeField('Date de publication')
    open = models.BooleanField(default=True)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Récement publié ?'

    def __str__(self):
        return self.question_text

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
        ordering = ["-pub_date"]


class Choix(models.Model):
    question = models.ForeignKey(Question)
    choix_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choix_text