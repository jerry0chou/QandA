# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20170501_1325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='comment',
        ),
        migrations.AddField(
            model_name='article',
            name='comment',
            field=models.ManyToManyField(default=b'', to='home.Comment', null=True, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba', blank=True),
        ),
        migrations.RemoveField(
            model_name='question',
            name='article',
        ),
        migrations.AddField(
            model_name='question',
            name='article',
            field=models.ManyToManyField(to='home.Article', null=True, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0', blank=True),
        ),
    ]
