# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0006_auto_20151120_2045'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonSurvey',
            fields=[
                ('personsurvey_id', models.AutoField(primary_key=True, serialize=False)),
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
            name='Survey',
            fields=[
                ('survey_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='SurveyQuestion',
            fields=[
                ('surveyquestion_id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.ForeignKey(to='survey.Question')),
                ('survey', models.ForeignKey(to='survey.Survey')),
            ],
        ),
        migrations.RenameModel(
            old_name='User',
            new_name='Person',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='user_age',
            new_name='person_age',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='user_id',
            new_name='person_id',
        ),
        migrations.RenameField(
            model_name='response',
            old_name='user_answer',
            new_name='response',
        ),
        migrations.RemoveField(
            model_name='response',
            name='question_text',
        ),
        migrations.RemoveField(
            model_name='response',
            name='user',
        ),
        migrations.AddField(
            model_name='personsurvey',
            name='person',
            field=models.ForeignKey(to='survey.Person'),
        ),
        migrations.AddField(
            model_name='personsurvey',
            name='survey',
            field=models.ForeignKey(to='survey.Survey'),
        ),
        migrations.AddField(
            model_name='response',
            name='personsurvey',
            field=models.ForeignKey(default=1, to='survey.PersonSurvey'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='response',
            name='surveyquestion',
            field=models.ForeignKey(default=1, to='survey.SurveyQuestion'),
            preserve_default=False,
        ),
    ]
