# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='comment',
            field=models.ForeignKey(default=b'', blank=True, to='home.Comment', null=True, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba'),
        ),
    ]
