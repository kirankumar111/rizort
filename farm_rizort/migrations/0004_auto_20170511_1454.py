# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm_rizort', '0003_auto_20170511_1313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nodes',
            name='id',
        ),
        migrations.AddField(
            model_name='nodes',
            name='node_id',
            field=models.IntegerField(default=1, serialize=False, primary_key=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='nodes',
            name='node_name',
            field=models.CharField(unique=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='node_1',
            field=models.ForeignKey(related_name='start_node', to='farm_rizort.Nodes', to_field=b'node_name'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='node_2',
            field=models.ForeignKey(related_name='end_node', to='farm_rizort.Nodes', to_field=b'node_name'),
        ),
    ]
