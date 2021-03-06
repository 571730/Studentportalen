# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-05 22:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Studentportalen', '0003_auto_20171104_1348'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vurdering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vanskelig', models.FloatField(default=0)),
                ('interesse', models.FloatField(default=0)),
                ('arbeid', models.FloatField(default=0)),
                ('kommentar', models.TextField(max_length=2000)),
                ('bruker', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
