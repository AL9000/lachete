# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_commentaire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentaire',
            name='titre',
            field=models.CharField(max_length=25),
            preserve_default=True,
        ),
    ]
