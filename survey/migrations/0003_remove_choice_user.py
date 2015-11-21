# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_choice_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='user',
        ),
    ]
