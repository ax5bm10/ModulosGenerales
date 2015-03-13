# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_agregacion', models.DateTimeField(auto_created=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('ci', models.IntegerField()),
                ('ruc', models.CharField(max_length=15)),
                ('celular', models.CharField(max_length=15)),
                ('mail', models.CharField(max_length=100)),
                ('fecha_ultima_modificacion', models.DateTimeField(auto_now=True)),
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
                ('barrio', models.TextField(max_length=15)),
                ('telefono', models.CharField(max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
