# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='costo_total',
            field=models.IntegerField(default=1, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productos',
            name='costo_unitario',
            field=models.IntegerField(default=1, blank=True),
            preserve_default=False,
        ),
    ]
