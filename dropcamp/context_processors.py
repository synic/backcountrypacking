from . import models

def link(request):
    links = models.Link.objects.order_by('position', 'id')
    return {
        'page_links': links,
    }
