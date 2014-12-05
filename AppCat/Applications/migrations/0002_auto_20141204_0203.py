# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Applications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='pic',
            field=models.URLField(),
            preserve_default=True,
        ),
    ]
