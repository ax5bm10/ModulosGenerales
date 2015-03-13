# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='ubicacion',
            field=models.ForeignKey(default=12, to='Clientes.Ubicacion'),
            preserve_default=False,
        ),
    ]
