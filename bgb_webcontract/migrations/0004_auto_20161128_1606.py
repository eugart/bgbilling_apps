# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bgb_webcontract', '0003_request_it_manager_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='rejection_reason',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
