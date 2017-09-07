# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-15 09:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScriptArgs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('args_name', models.CharField(default='', max_length=100)),
                ('args_value', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='script',
            name='script',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='scriptargs',
            name='script',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='operation.Script'),
        ),
    ]