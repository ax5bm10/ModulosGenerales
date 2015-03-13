# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0002_cliente_ubicacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='ubicacion',
        ),
        migrations.AddField(
            model_name='ubicacion',
            name='cliente',
            field=models.ForeignKey(default=1, to='Clientes.Cliente'),
            preserve_default=False,
        ),
    ]
