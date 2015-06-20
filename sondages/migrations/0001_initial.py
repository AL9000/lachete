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
            name='Choix',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('choix_text', models.CharField(max_length=200, verbose_name='choix')),
                ('votes', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'choix',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200, verbose_name='question')),
                ('slug', models.SlugField(max_length=200, unique=True, editable=False)),
                ('pub_date', models.DateField(help_text='Si la date est dans le futur, la question sera publiée à cette date.', verbose_name='date de publication')),
                ('open', models.BooleanField(verbose_name='question ouverte au vote ?', help_text='Décocher cette case pour fermer la question', default=True)),
                ('votants', models.ManyToManyField(to=settings.AUTH_USER_MODEL, editable=False)),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
                'ordering': ['-pub_date'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='choix',
            name='question',
            field=models.ForeignKey(to='sondages.Question'),
            preserve_default=True,
        ),
    ]
