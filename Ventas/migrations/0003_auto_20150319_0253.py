# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ventas', '0002_auto_20150317_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle_venta',
            name='descuento',
            field=models.IntegerField(blank=True),
            preserve_default=True,
        ),
    ]
