# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='category',
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.BooleanField(default=0, max_length=2, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(0, b'\xe7\x94\xb7'), (1, b'\xe5\xa5\xb3')]),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
