# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Stock', '0001_initial'),
        ('Compra', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField()),
                ('precio_unitario', models.IntegerField()),
                ('precio_total', models.IntegerField()),
                ('compra', models.ForeignKey(to='Compra.Compra')),
                ('producto', models.ForeignKey(to='Stock.Productos')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='compra',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='precio_total',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='precio_unitario',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='producto',
        ),
    ]
