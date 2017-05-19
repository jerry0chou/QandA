# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile',
            field=models.TextField(default=b'<img width="300" class="img-responsive img-thumbnail" src="/uploads/default/zhi.jpg" />', verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f'),
        ),
    ]
