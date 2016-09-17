# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-17 06:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('iiits', '0058_auto_20160714_0829'),
    ]

    operations = [
        migrations.CreateModel(
            name='WriteToUsQuery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('query', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='topstory',
            name='news_link',
        ),
        migrations.AddField(
            model_name='topstory',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 7, 17, 6, 9, 49, 6705, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='notice',
            name='valid_until',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 24, 6, 9, 20, 574739, tzinfo=utc)),
        ),
    ]
