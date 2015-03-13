# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Stock', '0001_initial'),
        ('Proveedores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField()),
                ('precio_unitario', models.IntegerField()),
                ('precio_total', models.IntegerField()),
                ('nro_comprobante', models.CharField(max_length=30)),
                ('fecha_compra', models.DateTimeField()),
                ('fecha_agregacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_ultima_modificacion', models.DateTimeField(auto_now=True)),
                ('producto', models.ForeignKey(to='Stock.Productos')),
                ('proveedor', models.ForeignKey(to='Proveedores.Proveedores')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
