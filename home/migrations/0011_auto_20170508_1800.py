# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20170506_1122'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='message',
            unique_together=set([]),
        ),
    ]
