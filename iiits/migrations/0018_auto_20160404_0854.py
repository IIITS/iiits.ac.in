# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-04 08:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iiits', '0017_facultypublication'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facultypublication',
            name='faculty',
        ),
        migrations.RemoveField(
            model_name='facultypublication',
            name='publication',
        ),
        migrations.AddField(
            model_name='publications',
            name='authors',
            field=models.TextField(default='NA'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='FacultyPublication',
        ),
    ]
