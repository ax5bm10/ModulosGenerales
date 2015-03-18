# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Facturacion', '0001_initial'),
        ('Ventas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venta',
            old_name='fecha_compra',
            new_name='fecha_venta',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='nro_comprobante',
        ),
        migrations.AddField(
            model_name='venta',
            name='factura',
            field=models.ForeignKey(to='Facturacion.Factura', null=True),
            preserve_default=True,
        ),
    ]
