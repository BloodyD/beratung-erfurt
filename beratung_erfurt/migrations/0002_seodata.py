# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beratung_erfurt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeoData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=255, verbose_name=b'Key')),
                ('description', models.TextField(verbose_name=b'Beschreibung')),
                ('keywords', models.TextField(verbose_name=b'Keywords')),
            ],
            options={
                'verbose_name': 'Seo Data',
                'verbose_name_plural': 'Seo Data',
            },
        ),
    ]
