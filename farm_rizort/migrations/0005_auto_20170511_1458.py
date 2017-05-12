# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm_rizort', '0004_auto_20170511_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nodes',
            name='node_id',
        ),
        migrations.AddField(
            model_name='nodes',
            name='node_cd',
            field=models.CharField(default=1234, max_length=200, serialize=False, primary_key=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='relationship',
            name='node_1',
            field=models.ForeignKey(related_name='start_node', to='farm_rizort.Nodes'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='node_2',
            field=models.ForeignKey(related_name='end_node', to='farm_rizort.Nodes'),
        ),
    ]
