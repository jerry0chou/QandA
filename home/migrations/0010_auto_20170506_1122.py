# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20170506_1038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='focus_num',
        ),
        migrations.AddField(
            model_name='question',
            name='likes',
            field=models.IntegerField(default=0, verbose_name=b'\xe5\x96\x9c\xe6\xac\xa2'),
        ),
    ]
