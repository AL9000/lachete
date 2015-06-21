# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(verbose_name='adresse email', max_length=255, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(verbose_name="nom d'utilisateur", max_length=20),
            preserve_default=True,
        ),
    ]
