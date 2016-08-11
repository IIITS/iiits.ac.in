# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-28 16:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iiits', '0034_auto_20160518_0522'),
    ]

    operations = [
        migrations.CreateModel(
            name='CareerFacultyPosition',
            fields=[
                ('career_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='iiits.Career')),
            ],
            bases=('iiits.career', models.Model),
        ),
    ]
