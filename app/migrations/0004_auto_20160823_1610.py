# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20160823_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='M2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f2', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='M1',
        ),
    ]
