# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Compra', '0003_auto_20150313_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle_compra',
            name='precio_total',
            field=models.IntegerField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='detalle_compra',
            name='precio_unitario',
            field=models.IntegerField(blank=True),
            preserve_default=True,
        ),
    ]
