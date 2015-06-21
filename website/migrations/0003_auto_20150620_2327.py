# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20150620_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='is_admin',
            field=models.BooleanField(verbose_name='membre de la chêteam', default=False),
            preserve_default=True,
        ),
    ]
