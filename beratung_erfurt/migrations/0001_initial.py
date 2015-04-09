# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Page'
        db.create_table(u'beratung_erfurt_page', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'beratung_erfurt', ['Page'])

        # Adding model 'Text'
        db.create_table(u'beratung_erfurt_text', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'beratung_erfurt', ['Text'])

        # Adding model 'Image'
        db.create_table(u'beratung_erfurt_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'beratung_erfurt', ['Image'])

        # Adding model 'SubPage'
        db.create_table(u'beratung_erfurt_subpage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('info', self.gf('django.db.models.fields.TextField')()),
            ('cause', self.gf('django.db.models.fields.TextField')()),
            ('solution', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'beratung_erfurt', ['SubPage'])


    def backwards(self, orm):
        # Deleting model 'Page'
        db.delete_table(u'beratung_erfurt_page')

        # Deleting model 'Text'
        db.delete_table(u'beratung_erfurt_text')

        # Deleting model 'Image'
        db.delete_table(u'beratung_erfurt_image')

        # Deleting model 'SubPage'
        db.delete_table(u'beratung_erfurt_subpage')


    models = {
        u'beratung_erfurt.image': {
            'Meta': {'object_name': 'Image'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'beratung_erfurt.page': {
            'Meta': {'object_name': 'Page'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'beratung_erfurt.subpage': {
            'Meta': {'object_name': 'SubPage'},
            'cause': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'solution': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'beratung_erfurt.text': {
            'Meta': {'object_name': 'Text'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['beratung_erfurt']