# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-16 06:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('two', '0002_auto_20181116_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=30)),
                ('group1', models.ManyToManyField(to='two.Group1')),
            ],
            options={
                'db_table': 'project',
            },
        ),
    ]
