# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-10-28 23:36
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('prisoner', '0020_auto_20181028_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='round',
            field=otree.db.models.IntegerField(default=1, null=True),
        ),
    ]