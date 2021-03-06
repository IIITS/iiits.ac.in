# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-07 14:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('iiits', '0053_auto_20160707_1414'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tender',
            fields=[
                ('notice_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='iiits.Notice')),
            ],
            bases=('iiits.notice', models.Model),
        ),
        migrations.CreateModel(
            name='TenderType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='notice',
            name='is_tender',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='tender_tags',
        ),
        migrations.AlterField(
            model_name='notice',
            name='valid_until',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 14, 14, 18, 36, 657235, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='tender',
            name='tender_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iiits.TenderType'),
        ),
    ]
