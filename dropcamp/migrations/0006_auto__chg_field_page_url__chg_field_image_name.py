# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Page.url'
        db.alter_column('dropcamp_page', 'url', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50))

        # Adding index on 'Page', fields ['url']
        db.create_index('dropcamp_page', ['url'])

        # Changing field 'Image.name'
        db.alter_column('dropcamp_image', 'name', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50))

        # Adding index on 'Image', fields ['name']
        db.create_index('dropcamp_image', ['name'])


    def backwards(self, orm):
        
        # Removing index on 'Image', fields ['name']
        db.delete_index('dropcamp_image', ['name'])

        # Removing index on 'Page', fields ['url']
        db.delete_index('dropcamp_page', ['url'])

        # Changing field 'Page.url'
        db.alter_column('dropcamp_page', 'url', self.gf('django.db.models.fields.CharField')(max_length=40, unique=True))

        # Changing field 'Image.name'
        db.alter_column('dropcamp_image', 'name', self.gf('django.db.models.fields.CharField')(max_length=40, unique=True))


    models = {
        'dropcamp.image': {
            'Meta': {'object_name': 'Image'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'package': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dropcamp.Package']", 'null': 'True', 'blank': 'True'})
        },
        'dropcamp.package': {
            'Meta': {'object_name': 'Package'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'}),
            'price': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'dropcamp.page': {
            'Meta': {'object_name': 'Page'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'large_image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'small_image_1': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'small_image_2': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'small_image_3': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['dropcamp']
