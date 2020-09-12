# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Page'
        db.create_table('dropcamp_page', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('large_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('small_image_1', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('small_image_2', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('small_image_3', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('dropcamp', ['Page'])


    def backwards(self, orm):
        
        # Deleting model 'Page'
        db.delete_table('dropcamp_page')


    models = {
        'dropcamp.page': {
            'Meta': {'object_name': 'Page'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'large_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'small_image_1': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'small_image_2': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'small_image_3': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        }
    }

    complete_apps = ['dropcamp']
