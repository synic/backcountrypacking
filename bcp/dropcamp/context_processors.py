from django.conf import settings

from . import models


def link(request):
    links = models.Link.objects.order_by('position', 'id')
    return {
        'page_links': links,
        'build_info': settings.BUILD_INFO,
    }
