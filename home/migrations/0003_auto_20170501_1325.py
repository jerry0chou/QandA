# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20170501_1220'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together=set([('follower', 'followee')]),
        ),
        migrations.AlterUniqueTogether(
            name='message',
            unique_together=set([('from_user', 'to_user')]),
        ),
    ]
