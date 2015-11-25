# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PickUp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('center', models.IntegerField()),
                ('klass', models.IntegerField()),
                ('student', models.IntegerField()),
                ('student_name', models.CharField(max_length=32)),
                ('pickup', models.CharField(max_length=32)),
                ('time', models.DateTimeField()),
            ],
        ),
    ]
