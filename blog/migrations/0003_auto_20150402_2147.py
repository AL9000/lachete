# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name_plural': 'Articles', 'verbose_name': 'Article', 'ordering': ['-date_de_parution']},
        ),
        migrations.AddField(
            model_name='article',
            name='date_de_modification',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 4, 2, 19, 47, 33, 107399, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='ouvert',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(unique=True, default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='date_de_parution',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(null=True, blank=True, upload_to='images/'),
            preserve_default=True,
        ),
    ]
