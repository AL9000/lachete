# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20150620_1104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentaire',
            name='date_de_modification',
        ),
    ]
