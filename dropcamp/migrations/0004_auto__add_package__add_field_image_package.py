# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Package'
        db.create_table('dropcamp_package', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('price', self.gf('django.db.models.fields.FloatField')(default=0.0)),
        ))
        db.send_create_signal('dropcamp', ['Package'])

        # Adding field 'Image.package'
        db.add_column('dropcamp_image', 'package', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dropcamp.Package'], null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'Package'
        db.delete_table('dropcamp_package')

        # Deleting field 'Image.package'
        db.delete_column('dropcamp_image', 'package_id')


    models = {
        'dropcamp.image': {
            'Meta': {'object_name': 'Image'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'package': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dropcamp.Package']", 'null': 'True', 'blank': 'True'})
        },
        'dropcamp.package': {
            'Meta': {'object_name': 'Package'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
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
            'url': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        }
    }

    complete_apps = ['dropcamp']
