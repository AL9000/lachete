# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sondages', '0008_auto_20150620_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateField(help_text='Si la date est dans le futur, la question sera publiée à cette date.', verbose_name='date de publication'),
            preserve_default=True,
        ),
    ]
