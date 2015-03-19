# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0004_auto_20150313_1423'),
        ('Facturacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_servicio', models.DateTimeField()),
                ('fecha_agregacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_ultima_modificacion', models.DateTimeField(auto_now=True)),
                ('cliente', models.ForeignKey(to='Clientes.Cliente')),
                ('factura', models.ForeignKey(to='Facturacion.Factura')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100)),
                ('definicion', models.TextField(max_length=1000)),
                ('precio', models.IntegerField()),
                ('descuento', models.IntegerField(blank=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('servicio', models.ForeignKey(to='Servicios.Servicio')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
