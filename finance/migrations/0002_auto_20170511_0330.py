# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-05-10 22:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockinfo',
            name='ticker',
            field=models.CharField(max_length=20),
        ),
    ]
