# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-01-22 02:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20190121_1701'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RolePerRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_id', models.IntegerField()),
                ('perm_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserRoleRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('role_id', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='permission',
            name='level',
        ),
        migrations.RemoveField(
            model_name='user',
            name='prem_id',
        ),
    ]
