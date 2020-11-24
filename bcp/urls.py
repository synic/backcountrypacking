from django.urls import include, path, re_path

from django.contrib import admin
from django.conf import settings

from bcp.dropcamp import views

urlpatterns = [
    path('', views.viewpage, {'path': '/home'}, name='index'),
    re_path(r'^.admin/', admin.site.urls),
    path('', include('bcp.dropcamp.urls', namespace='dc')),
]
