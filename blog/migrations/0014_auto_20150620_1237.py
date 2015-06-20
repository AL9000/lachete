# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_article_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='video',
            field=models.URLField(help_text="Copie/colle l'url d'une vidéo YouTube ici et elle sera insérée à la fin de l'article.", blank=True),
            preserve_default=True,
        ),
    ]
