# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('farm_rizort', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drawingroom',
            name='drawing_room',
            field=models.CharField(default=datetime.datetime(2017, 5, 11, 11, 29, 41, 521723, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
