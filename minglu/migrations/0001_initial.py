# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ssjibenxinxi2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zch', models.TextField()),
                ('mcyename', models.TextField()),
                ('fddbri', models.TextField()),
                ('zyxmlb', models.TextField()),
                ('dz', models.TextField()),
                ('rjzczb', models.TextField()),
                ('qylx', models.TextField()),
                ('clrq', models.TextField()),
                ('yyqx', models.TextField()),
                ('hzrq', models.TextField()),
                ('djjg', models.TextField()),
                ('zt', models.TextField()),
                ('jyfw', models.TextField()),
            ],
        ),
    ]
