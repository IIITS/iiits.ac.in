# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-29 21:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iiits', '0042_auto_20160529_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='show_achievements',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='faculty',
            name='show_contact_no',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='faculty',
            name='show_other_info',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='faculty',
            name='show_website',
            field=models.BooleanField(default=True),
        ),
    ]
