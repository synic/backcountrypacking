from django import template
from django.db import models

from bcp.dropcamp.models import Image

register = template.Library()

class ImageNode(template.Node):
    def __init__(self, name, item_name, nodelist):
        self.name = name
        self.item_name = item_name
        self.nodelist = nodelist

    def render(self, context):
        try:
            content = Image.objects.get(name=self.name)
        except Image.DoesNotExist:
            content = None
        context.push()
        context[self.item_name] = content
        output = self.nodelist.render(context)
        context.pop()
        return output

@register.tag('dcimage')
def do_dcimage(parser, token):
    bits = token.split_contents()
    remaining_bits = bits[1:]

    (name, item_name) = remaining_bits
    nodelist = parser.parse(('enddcimage',))
    parser.delete_first_token()

    return ImageNode(name, item_name, nodelist)
