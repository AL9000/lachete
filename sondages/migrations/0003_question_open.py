# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sondages', '0002_auto_20150319_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='open',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
