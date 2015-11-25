# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pickup',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 11, 24, 8, 56, 25, 672762, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pickup',
            name='time',
            field=models.CharField(max_length=16),
        ),
    ]
