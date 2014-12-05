# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Applications', '0002_auto_20141204_0203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app',
            name='rating',
        ),
        migrations.AlterField(
            model_name='app',
            name='pic',
            field=models.URLField(default=b'http://i.imgur.com/E2Mwfu5.png'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='app',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 4, 5, 22, 31, 273244, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=True,
        ),
    ]
