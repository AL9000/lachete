from django.db import models


class Categorie(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom


class Article(models.Model):
    titre = models.CharField(max_length=50)
    contenu = models.TextField()
    date_de_parution = models.DateTimeField()
    # image = models.ImageField()
    categorie = models.ForeignKey(Categorie)

    def __str__(self):
        return self.titre