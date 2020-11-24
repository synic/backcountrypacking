from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

from bcp.dropcamp import views

urlpatterns = [
    path('', views.viewpage, {'path': '/home'}, name='index'),
    re_path(r'^.admin/', admin.site.urls),
    path('', include('bcp.dropcamp.urls', namespace='dc')),
]

# The following allows static/media files to be served by django during
# development.
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT,
    )
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
