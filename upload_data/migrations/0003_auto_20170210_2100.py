# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 21:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_data', '0002_auto_20170209_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='username',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='description',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
