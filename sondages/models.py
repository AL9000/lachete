from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
import itertools


class Question(models.Model):
    question_text = models.CharField('question', max_length=200)
    slug = models.SlugField(max_length=200, unique=True, editable=False)
    pub_date = models.DateField('date de publication', help_text="Si la date est dans le futur, "
                                                                 "la question sera publiée à cette date.")
    open = models.BooleanField('question ouverte au vote ?', default=True, help_text='Décocher cette case pour fermer '
                                                                                     'la question')
    votants = models.ManyToManyField(User, editable=False)

    def __str__(self):
        return self.question_text

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
        ordering = ["-pub_date"]

    def save(self, *args, **kwargs):
        self.slug = orig = slugify(self.question_text)
        for x in itertools.count(1):
            if not Question.objects.filter(slug=self.slug).exists():
                break
            self.slug = '%s-%d' % (orig, x)
        super(Question, self).save(*args, **kwargs)


class Choix(models.Model):
    question = models.ForeignKey(Question)
    choix_text = models.CharField('choix', max_length=200)
    votes = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "choix"

    def __str__(self):
        return self.choix_text