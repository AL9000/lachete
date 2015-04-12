# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='test',
            field=models.ManyToManyField(to='blog.Categorie', related_name='test'),
            preserve_default=True,
        ),
    ]
