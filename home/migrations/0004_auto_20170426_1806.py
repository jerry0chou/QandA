# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20170426_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name=b'\xe9\x97\xae\xe9\xa2\x98\xe5\x90\x8d')),
                ('desc', models.CharField(max_length=50, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('date_publish', models.DateTimeField(verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4')),
                ('focus_num', models.IntegerField(default=0, verbose_name=b'\xe5\x85\xb3\xe6\xb3\xa8\xe9\x87\x8f')),
            ],
            options={
                'ordering': ['-date_publish'],
                'verbose_name': '\u95ee\u9898',
                'verbose_name_plural': '\u95ee\u9898',
            },
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=256, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe6\xa0\x87\xe9\xa2\x98'),
        ),
        migrations.AddField(
            model_name='question',
            name='article',
            field=models.ForeignKey(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0', to='home.Article'),
        ),
    ]
