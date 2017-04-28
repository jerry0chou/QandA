# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20170426_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='article',
            field=models.ForeignKey(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0', blank=True, to='home.Article', null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=128, verbose_name=b'\xe9\x97\xae\xe9\xa2\x98\xe5\x90\x8d'),
        ),
    ]
