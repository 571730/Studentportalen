# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-03 16:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Studentportalen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studie',
            name='beskrivelse',
            field=models.TextField(max_length=1000),
        ),
    ]
