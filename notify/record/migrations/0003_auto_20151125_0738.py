# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0002_auto_20151124_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pickup',
            name='pickup',
            field=models.CharField(max_length=32, null=True, blank=True),
        ),
    ]
