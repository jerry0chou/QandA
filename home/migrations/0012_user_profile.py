# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20170508_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile',
            field=models.TextField(default=b'', verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f'),
        ),
    ]
