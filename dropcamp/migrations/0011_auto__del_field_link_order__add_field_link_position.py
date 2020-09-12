# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Link.order'
        db.delete_column('dropcamp_link', 'order')

        # Adding field 'Link.position'
        db.add_column('dropcamp_link', 'position', self.gf('django.db.models.fields.PositiveIntegerField')(default=0), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Link.order'
        db.add_column('dropcamp_link', 'order', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Deleting field 'Link.position'
        db.delete_column('dropcamp_link', 'position')


    models = {
        'dropcamp.image': {
            'Meta': {'object_name': 'Image'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '50', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'package': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dropcamp.Package']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'dropcamp.link': {
            'Meta': {'ordering': "['position']", 'object_name': 'Link'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'position': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'dropcamp.package': {
            'Meta': {'object_name': 'Package'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'}),
            'price': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '40', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'dropcamp.page': {
            'Meta': {'object_name': 'Page'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'large_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'page_set1'", 'null': 'True', 'to': "orm['dropcamp.Image']"}),
            'small_image_1': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'page_set2'", 'null': 'True', 'to': "orm['dropcamp.Image']"}),
            'small_image_2': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'page_set3'", 'null': 'True', 'to': "orm['dropcamp.Image']"}),
            'small_image_3': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'page_set4'", 'null': 'True', 'to': "orm['dropcamp.Image']"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['dropcamp']
