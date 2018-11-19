# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-14 09:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('uname', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=32)),
                ('type', models.IntegerField(choices=[(1, '超级管理员'), (2, '普通用户')], default=2)),
                ('regtime', models.DateTimeField(default=django.utils.timezone.now)),
                ('ip', models.IntegerField(null=True)),
                ('allowed', models.IntegerField(choices=[(1, '允许登录'), (2, '禁止登录')], default=1)),
                ('email', models.CharField(max_length=100, null=True)),
                ('memo', models.CharField(max_length=1000, null=True)),
            ],
        ),
    ]