# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=255, verbose_name=b'Key')),
                ('image', models.ImageField(upload_to=b'image_upload')),
            ],
            options={
                'verbose_name': 'Bild',
                'verbose_name_plural': 'Bilder',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name=b'Titel')),
                ('path', models.CharField(max_length=255, verbose_name=b'Pfad')),
                ('content', models.TextField(verbose_name=b'Inhalt')),
                ('active', models.BooleanField(verbose_name=b'Aktiv')),
            ],
            options={
                'verbose_name': 'Seite',
                'verbose_name_plural': 'Seiten',
            },
        ),
        migrations.CreateModel(
            name='SubPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=255, verbose_name=b'Key')),
                ('title', models.CharField(max_length=255, verbose_name=b'Titel')),
                ('info', models.TextField(verbose_name=b'Info')),
                ('cause', models.TextField(verbose_name=b'Ursache')),
                ('solution', models.TextField(verbose_name=b'L\xc3\xb6sung')),
            ],
            options={
                'verbose_name': 'Unterseite',
                'verbose_name_plural': 'Unterseiten',
            },
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=255, verbose_name=b'Key')),
                ('content', models.TextField(verbose_name=b'Inhalt')),
            ],
            options={
                'verbose_name': 'Text',
                'verbose_name_plural': 'Texte',
            },
        ),
    ]
