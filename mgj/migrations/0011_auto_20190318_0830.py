# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-18 08:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mgj', '0010_order_ordermoney'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetail',
            name='oldprice',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='productdetail',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
