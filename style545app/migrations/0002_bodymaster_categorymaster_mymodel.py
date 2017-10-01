# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('style545app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Bodymaster',
            fields=[
            ],
            options={
                'db_table': 'BODYMASTER',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Categorymaster',
            fields=[
            ],
            options={
                'db_table': 'CATEGORYMASTER',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
