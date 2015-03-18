# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nro_factura', models.CharField(max_length=100)),
                ('fecha_factura', models.DateTimeField()),
                ('fecha_agregacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_ultima_modificacion', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
