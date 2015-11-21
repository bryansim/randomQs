# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0005_auto_20151120_2040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('response_id', models.AutoField(serialize=False, primary_key=True)),
                ('question_text', models.CharField(max_length=200)),
                ('user_answer', models.IntegerField(default=0)),
                ('user', models.ForeignKey(to='survey.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='user',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
