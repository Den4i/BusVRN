# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 07:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manuals', '0010_auto_20160323_1653'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='name',
            new_name='name_proj',
        ),
        migrations.RenameField(
            model_name='route',
            old_name='name',
            new_name='name_route',
        ),
    ]
