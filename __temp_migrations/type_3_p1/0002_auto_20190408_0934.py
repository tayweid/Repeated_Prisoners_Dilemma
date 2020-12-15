# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-04-08 13:34
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('type_3_p1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='cycle',
        ),
        migrations.RemoveField(
            model_name='player',
            name='cycle',
        ),
        migrations.RemoveField(
            model_name='player',
            name='other_decision',
        ),
        migrations.RemoveField(
            model_name='player',
            name='round',
        ),
        migrations.AddField(
            model_name='group',
            name='p1_cycle',
            field=otree.db.models.IntegerField(default=1, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='group_decision',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='p1_cycle',
            field=otree.db.models.IntegerField(default=1, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='p1_round',
            field=otree.db.models.IntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='decision',
            field=otree.db.models.StringField(choices=[('Green', 'Green'), ('Red', 'Red')], max_length=10000, null=True),
        ),
    ]