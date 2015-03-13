# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Stock', '0001_initial'),
        ('Compra', '0002_auto_20150313_1907'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle_Compra',
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
            model_name='detalle',
            name='compra',
        ),
        migrations.RemoveField(
            model_name='detalle',
            name='producto',
        ),
        migrations.DeleteModel(
            name='Detalle',
        ),
    ]
