# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-17 23:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('iiits', '0063_auto_20160717_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='valid_until',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 24, 23, 25, 13, 501420, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='researchcentreprofile',
            name='faculty',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='researchcentreprofile',
            name='people',
            field=models.TextField(default=''),
        ),
    ]
