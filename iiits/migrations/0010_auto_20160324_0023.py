# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-24 00:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iiits', '0009_admissionsfeestructure_academic_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admissionsfinancialassistance',
            name='order_no',
            field=models.PositiveIntegerField(db_index=True),
        ),
    ]
