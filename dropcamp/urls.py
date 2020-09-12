from django.views.generic import DetailView
from django.conf.urls.defaults import url, patterns
from . import models
from . import views

urlpatterns = patterns('dropcamp.views',
    url(r'^contact/$', views.ContactView.as_view(), name='contact'),
    url(r'^(?P<package_type>areas|packages)/$', 
        views.PackagesView.as_view(), name='packages'),
    url(r'^p/(?P<slug>[\w-]+)/$',
        DetailView.as_view(
            model=models.Package),
        name='viewpackage'),
)
