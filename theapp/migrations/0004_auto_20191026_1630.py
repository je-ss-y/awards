# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-26 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0003_auto_20191026_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snap',
            name='description',
            field=models.TextField(),
        ),
    ]
