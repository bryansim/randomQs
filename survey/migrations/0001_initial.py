# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('question_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_age', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='user',
            field=models.ForeignKey(to='survey.User'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='survey.Question'),
        ),
    ]
