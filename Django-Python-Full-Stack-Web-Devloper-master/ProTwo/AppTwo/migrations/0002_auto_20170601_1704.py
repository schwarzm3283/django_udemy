# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-01 21:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTwo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=264, unique=True),
        ),
    ]