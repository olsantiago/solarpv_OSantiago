# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-07 23:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20191120_0134'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=20),
        ),
    ]
