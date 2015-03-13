# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0003_auto_20150312_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ubicacion',
            name='telefono',
        ),
        migrations.AddField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_agregacion',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
