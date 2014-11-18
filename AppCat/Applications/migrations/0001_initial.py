# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app_name', models.CharField(max_length=100)),
                ('developers', models.CharField(default=b'Anonymous', max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('description', models.TextField(default=b'An App')),
                ('link', models.URLField()),
                ('pic', models.FileField(default=b'images/App_pic/no_icon.png', upload_to=b'images/App_pic')),
                ('rating', models.DecimalField(max_digits=3, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('review_name', models.CharField(max_length=100)),
                ('description', models.TextField(default=b'')),
                ('rating', models.DecimalField(max_digits=1, decimal_places=0)),
                ('app', models.ForeignKey(to='Applications.App')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
