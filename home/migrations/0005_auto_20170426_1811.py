# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20170426_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='desc',
            field=models.TextField(max_length=256, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe6\x8f\x8f\xe8\xbf\xb0'),
        ),
    ]
