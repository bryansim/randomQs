# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_remove_choice_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='user',
            field=models.ForeignKey(default=1, to='survey.User'),
            preserve_default=False,
        ),
    ]
