# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_remove_commentaire_date_de_modification'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='video',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
    ]
