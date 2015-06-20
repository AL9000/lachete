# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sondages', '0007_auto_20150620_1257'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='choix',
            options={'verbose_name_plural': 'choix'},
        ),
        migrations.AlterField(
            model_name='choix',
            name='choix_text',
            field=models.CharField(verbose_name='choix', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='open',
            field=models.BooleanField(default=True, verbose_name='question ouverte au vote ?', help_text='Décocher cette case pour fermer la question'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateField(verbose_name='date de publication'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(verbose_name='question', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='votants',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, editable=False),
            preserve_default=True,
        ),
    ]
