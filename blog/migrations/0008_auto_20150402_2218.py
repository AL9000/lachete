# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_article_categorie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='test',
        ),
        migrations.AddField(
            model_name='article',
            name='categorie',
            field=models.ManyToManyField(to='blog.Categorie'),
            preserve_default=True,
        ),
    ]
