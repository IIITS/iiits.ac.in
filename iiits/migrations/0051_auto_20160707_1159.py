# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-07 11:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('iiits', '0050_campuslifeentity_rank'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='noticeno',
        ),
        migrations.AddField(
            model_name='notice',
            name='description',
            field=models.TextField(default='NA'),
        ),
        migrations.AddField(
            model_name='notice',
            name='valid_until',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 14, 11, 59, 21, 523231, tzinfo=utc)),
        ),
    ]
