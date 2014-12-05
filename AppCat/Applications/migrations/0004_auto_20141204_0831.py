# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Applications', '0003_auto_20141204_0522'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='approved',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='app',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 4, 8, 31, 1, 459129, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=True,
        ),
    ]
