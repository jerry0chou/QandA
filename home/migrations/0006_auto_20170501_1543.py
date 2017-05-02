# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20170501_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='comment',
        ),
        migrations.AddField(
            model_name='article',
            name='comment',
            field=models.ManyToManyField(to='home.Comment', null=True, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba', blank=True),
        ),
    ]
