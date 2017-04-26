# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20170426_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(default=b'', max_length=50, verbose_name=b'\xe6\x98\xb5\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='user',
            name='self_description',
            field=models.CharField(default=b'\xe6\x88\x91\xe4\xbb\x80\xe4\xb9\x88\xe9\x83\xbd\xe6\xb2\xa1\xe5\x86\x99', max_length=256, verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0'),
        ),
    ]
