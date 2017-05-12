# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BeachResort',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('arrival_dt', models.DateTimeField(auto_now=True)),
                ('dept_dt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DrawingRoom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('pool_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='drawingroom',
            name='swimming_pool',
            field=models.ForeignKey(to='farm_rizort.Pool'),
        ),
        migrations.AddField(
            model_name='beachresort',
            name='drawing_room',
            field=models.ForeignKey(to='farm_rizort.DrawingRoom'),
        ),
        migrations.AddField(
            model_name='beachresort',
            name='swimming_pool',
            field=models.ForeignKey(to='farm_rizort.Pool'),
        ),
    ]
