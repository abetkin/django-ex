# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20160823_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='M4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='M5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='M1',
        ),
        migrations.DeleteModel(
            name='M2',
        ),
    ]
