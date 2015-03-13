# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('ruc', models.CharField(max_length=15)),
                ('telefono', models.CharField(max_length=15)),
                ('celular', models.CharField(max_length=15)),
                ('mail', models.CharField(max_length=100)),
                ('fecha_agregacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('calle', models.CharField(max_length=100)),
                ('nro', models.IntegerField()),
                ('barrio', models.CharField(max_length=15)),
                ('proveedor', models.ForeignKey(to='Proveedores.Proveedores')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
