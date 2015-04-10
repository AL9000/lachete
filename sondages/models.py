from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    pub_date = models.DateTimeField('Date de publication')
    open = models.BooleanField(default=True)
    votants = models.ManyToManyField(User)

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