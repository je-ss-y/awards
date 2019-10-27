# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-27 09:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0005_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='snap',
            name='content',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='snap',
            name='design',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='snap',
            name='link',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='snap',
            name='usability',
            field=models.IntegerField(default=0),
        ),
    ]
