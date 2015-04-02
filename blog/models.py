from django.db import models


class Categorie(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom


class ArticleQuerySet(models.QuerySet):
    def published(self):
        return self.filter(ouvert=True)


class Article(models.Model):
    titre = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True)
    categorie = models.ForeignKey(Categorie)
    ouvert = models.BooleanField(default=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    date_de_parution = models.DateTimeField(auto_now_add=True)
    date_de_modification = models.DateTimeField(auto_now=True)
    contenu = models.TextField()

    objects = ArticleQuerySet.as_manager()

    def __str__(self):
        return self.titre

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ["-date_de_parution"]