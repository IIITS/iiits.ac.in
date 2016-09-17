# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-04 08:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iiits', '0016_auto_20160402_0536'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyPublication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iiits.Faculty')),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iiits.Publications')),
            ],
        ),
    ]
