# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0008_auto_20150402_2218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('titre', models.CharField(max_length=50)),
                ('contenu', models.TextField()),
                ('date_de_parution', models.DateTimeField(auto_now_add=True)),
                ('date_de_modification', models.DateTimeField(auto_now=True)),
                ('article', models.ForeignKey(to='blog.Article')),
                ('utilisateur', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
