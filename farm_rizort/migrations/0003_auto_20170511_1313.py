# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm_rizort', '0002_drawingroom_drawing_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nodes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('node_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link_name', models.CharField(max_length=50)),
                ('node_1', models.ForeignKey(related_name='start_node', to='farm_rizort.Nodes')),
                ('node_2', models.ForeignKey(related_name='end_node', to='farm_rizort.Nodes')),
            ],
        ),
        migrations.RemoveField(
            model_name='beachresort',
            name='drawing_room',
        ),
        migrations.RemoveField(
            model_name='beachresort',
            name='swimming_pool',
        ),
        migrations.RemoveField(
            model_name='drawingroom',
            name='swimming_pool',
        ),
        migrations.DeleteModel(
            name='BeachResort',
        ),
        migrations.DeleteModel(
            name='DrawingRoom',
        ),
        migrations.DeleteModel(
            name='Pool',
        ),
    ]
