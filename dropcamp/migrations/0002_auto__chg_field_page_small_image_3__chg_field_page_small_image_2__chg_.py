# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Page.small_image_3'
        db.alter_column('dropcamp_page', 'small_image_3', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True))

        # Changing field 'Page.small_image_2'
        db.alter_column('dropcamp_page', 'small_image_2', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True))

        # Changing field 'Page.small_image_1'
        db.alter_column('dropcamp_page', 'small_image_1', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True))

        # Changing field 'Page.large_image'
        db.alter_column('dropcamp_page', 'large_image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True))


    def backwards(self, orm):
        
        # User chose to not deal with backwards NULL issues for 'Page.small_image_3'
        raise RuntimeError("Cannot reverse this migration. 'Page.small_image_3' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Page.small_image_2'
        raise RuntimeError("Cannot reverse this migration. 'Page.small_image_2' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Page.small_image_1'
        raise RuntimeError("Cannot reverse this migration. 'Page.small_image_1' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Page.large_image'
        raise RuntimeError("Cannot reverse this migration. 'Page.large_image' and its values cannot be restored.")


    models = {
        'dropcamp.page': {
            'Meta': {'object_name': 'Page'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'large_image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'small_image_1': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'small_image_2': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'small_image_3': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        }
    }

    complete_apps = ['dropcamp']
