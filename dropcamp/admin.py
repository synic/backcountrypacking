from django.contrib import admin
from django import forms
from dragorder.admin import OrderableStackedInline
from . import models

class PageAdmin(admin.ModelAdmin):
    list_display = ('url', 'title')

admin.site.register(models.Page, PageAdmin)

class ImageForm(forms.ModelForm):
    class Meta:
        model = models.Image

    def clean_name(self):
        name = self.cleaned_data['name']
        if not name:
            name = None

        return name

class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'package')

    form = ImageForm

admin.site.register(models.Image, ImageAdmin)

class ImageInline(admin.TabularInline):
    model = models.Image
    form = ImageForm

class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'title', 'type', 'price')
    inlines = [
        ImageInline,
    ]
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(models.Package, PackageAdmin)

class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title', 'url', 'position')
    list_editable = ('position', 'name', 'title', 'url')
    
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1/jquery-ui.min.js',
            'static/admin_list_ordering.js', 
        )

admin.site.register(models.Link, LinkAdmin)
