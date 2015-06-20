# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=200, unique=True, editable=False)),
                ('ouvert', models.BooleanField(default=True)),
                ('date_de_parution', models.DateTimeField(auto_now_add=True)),
                ('date_de_modification', models.DateTimeField(auto_now=True)),
                ('contenu', models.TextField()),
                ('video', models.URLField(blank=True, help_text="Copie/colle l'url d'une vidéo YouTube ici et elle sera insérée à la fin de l'article.")),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
                'ordering': ['-date_de_parution'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nom', models.SlugField(max_length=200, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('titre', models.CharField(max_length=25)),
                ('contenu', models.TextField()),
                ('date_de_parution', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(to='blog.Article')),
                ('utilisateur', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='categorie',
            field=models.ManyToManyField(to='blog.Categorie'),
            preserve_default=True,
        ),
    ]
