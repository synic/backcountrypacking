from django.urls import re_path
from django.views.generic import DetailView

from . import models
from . import views

app_name = 'dropcamp'

urlpatterns = [
    re_path(r'^contact/$', views.ContactView.as_view(), name='contact'),
    re_path(
        r'^(?P<package_type>areas|packages)/$',
        views.PackagesView.as_view(),
        name='packages',
    ),
    re_path(r'^(?P<path>\w+)/$', views.viewpage, name='page'),
    re_path(
        r'^p/(?P<slug>[\w-]+)/$',
        DetailView.as_view(model=models.Package),
        name='viewpackage',
    ),
]
