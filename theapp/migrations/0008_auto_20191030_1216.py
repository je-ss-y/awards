# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-30 09:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0007_auto_20191027_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='snap',
            name='content',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0),
        ),
        migrations.AddField(
            model_name='snap',
            name='design',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0),
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
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0),
        ),
        migrations.AddField(
            model_name='snap',
            name='vote_submissions',
            field=models.IntegerField(default=0),
        ),
    ]
