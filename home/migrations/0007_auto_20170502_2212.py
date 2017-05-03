# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20170501_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='user',
            field=models.ForeignKey(verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL),
        ),
    ]
