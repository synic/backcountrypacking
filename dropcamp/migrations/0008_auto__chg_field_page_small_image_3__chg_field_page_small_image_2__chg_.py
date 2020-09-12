# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Renaming column for 'Page.small_image_3' to match new field type.
        db.rename_column('dropcamp_page', 'small_image_3', 'small_image_3_id')
        # Changing field 'Page.small_image_3'
        db.alter_column('dropcamp_page', 'small_image_3_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['dropcamp.Image']))

        # Adding index on 'Page', fields ['small_image_3']
        db.create_index('dropcamp_page', ['small_image_3_id'])

        # Renaming column for 'Page.small_image_2' to match new field type.
        db.rename_column('dropcamp_page', 'small_image_2', 'small_image_2_id')
        # Changing field 'Page.small_image_2'
        db.alter_column('dropcamp_page', 'small_image_2_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['dropcamp.Image']))

        # Adding index on 'Page', fields ['small_image_2']
        db.create_index('dropcamp_page', ['small_image_2_id'])

        # Renaming column for 'Page.small_image_1' to match new field type.
        db.rename_column('dropcamp_page', 'small_image_1', 'small_image_1_id')
        # Changing field 'Page.small_image_1'
        db.alter_column('dropcamp_page', 'small_image_1_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['dropcamp.Image']))

        # Adding index on 'Page', fields ['small_image_1']
        db.create_index('dropcamp_page', ['small_image_1_id'])

        # Renaming column for 'Page.large_image' to match new field type.
        db.rename_column('dropcamp_page', 'large_image', 'large_image_id')
        # Changing field 'Page.large_image'
        db.alter_column('dropcamp_page', 'large_image_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['dropcamp.Image']))

        # Adding index on 'Page', fields ['large_image']
        db.create_index('dropcamp_page', ['large_image_id'])


    def backwards(self, orm):
        
        # Removing index on 'Page', fields ['large_image']
        db.delete_index('dropcamp_page', ['large_image_id'])

        # Removing index on 'Page', fields ['small_image_1']
        db.delete_index('dropcamp_page', ['small_image_1_id'])

        # Removing index on 'Page', fields ['small_image_2']
        db.delete_index('dropcamp_page', ['small_image_2_id'])

        # Removing index on 'Page', fields ['small_image_3']
        db.delete_index('dropcamp_page', ['small_image_3_id'])

        # Renaming column for 'Page.small_image_3' to match new field type.
        db.rename_column('dropcamp_page', 'small_image_3_id', 'small_image_3')
        # Changing field 'Page.small_image_3'
        db.alter_column('dropcamp_page', 'small_image_3', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True))

        # Renaming column for 'Page.small_image_2' to match new field type.
        db.rename_column('dropcamp_page', 'small_image_2_id', 'small_image_2')
        # Changing field 'Page.small_image_2'
        db.alter_column('dropcamp_page', 'small_image_2', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True))

        # Renaming column for 'Page.small_image_1' to match new field type.
        db.rename_column('dropcamp_page', 'small_image_1_id', 'small_image_1')
        # Changing field 'Page.small_image_1'
        db.alter_column('dropcamp_page', 'small_image_1', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True))

        # Renaming column for 'Page.large_image' to match new field type.
        db.rename_column('dropcamp_page', 'large_image_id', 'large_image')
        # Changing field 'Page.large_image'
        db.alter_column('dropcamp_page', 'large_image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True))


    models = {
        'dropcamp.image': {
            'Meta': {'object_name': 'Image'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '50', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'package': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dropcamp.Package']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
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
