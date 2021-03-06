# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-04 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Studentportalen', '0002_auto_20171103_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='emne',
            name='arbeid',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='emne',
            name='beskrivelse',
            field=models.CharField(default='Beskrivelse av faget', max_length=300),
        ),
        migrations.AddField(
            model_name='emne',
            name='interesse',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='emne',
            name='vanskelig',
            field=models.FloatField(default=0),
        ),
    ]
