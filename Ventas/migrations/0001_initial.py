# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Stock', '0001_initial'),
        ('Clientes', '0004_auto_20150313_1423'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle_Venta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('descuento', models.IntegerField()),
                ('producto', models.ForeignKey(to='Stock.Productos')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nro_comprobante', models.CharField(max_length=30)),
                ('fecha_compra', models.DateTimeField()),
                ('fecha_agregacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_ultima_modificacion', models.DateTimeField(auto_now=True)),
                ('cliente', models.ForeignKey(to='Clientes.Cliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='detalle_venta',
            name='venta',
            field=models.ForeignKey(to='Ventas.Venta'),
            preserve_default=True,
        ),
    ]
