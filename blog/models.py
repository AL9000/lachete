from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
import itertools


class Categorie(models.Model):
    nom = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.nom


class ArticleQuerySet(models.QuerySet):
    def published(self):
        return self.filter(ouvert=True)


class Article(models.Model):
    titre = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True, editable=False)
    categorie = models.ManyToManyField(Categorie)
    ouvert = models.BooleanField(default=True)
    date_de_parution = models.DateTimeField(auto_now_add=True, editable=False)
    date_de_modification = models.DateTimeField(auto_now=True)
    contenu = models.TextField()
    video = models.URLField(blank=True, help_text="Copie/colle l'url d'une vidéo YouTube ici et elle sera "
                                                  "insérée à la fin de l'article.")

    objects = ArticleQuerySet.as_manager()

    def __str__(self):
        return self.titre

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ["-date_de_parution"]

    def save(self, *args, **kwargs):
        self.slug = orig = slugify(self.titre)
        for x in itertools.count(1):
            if not Article.objects.filter(slug=self.slug).exists():
                break
            self.slug = '%s-%d' % (orig, x)
        self.video = self.video.replace('watch?v=', 'embed/')
        super(Article, self).save(*args, **kwargs)


class Commentaire(models.Model):
    titre = models.CharField(max_length=25)
    contenu = models.TextField()
    article = models.ForeignKey(Article)
    utilisateur = models.ForeignKey(User)
    date_de_parution = models.DateTimeField(auto_now_add=True)