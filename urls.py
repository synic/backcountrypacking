from django.conf.urls.defaults import *

from django.contrib import admin
from django.conf import settings

from dropcamp import views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.viewpage, {'path': '/home'}, name='index'),
    (r'^.admin/', include(admin.site.urls)),
    url(r'^', include('dropcamp.urls', namespace='dc')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 
            'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT}),
    )
