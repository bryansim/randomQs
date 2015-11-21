# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='user',
            field=models.ForeignKey(to='survey.User', default=1),
            preserve_default=False,
        ),
    ]
