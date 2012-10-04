# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UploadedFile'
        db.create_table('simple_file_sender_uploadedfile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('data', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('simple_file_sender', ['UploadedFile'])


    def backwards(self, orm):
        # Deleting model 'UploadedFile'
        db.delete_table('simple_file_sender_uploadedfile')


    models = {
        'simple_file_sender.uploadedfile': {
            'Meta': {'object_name': 'UploadedFile'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['simple_file_sender']