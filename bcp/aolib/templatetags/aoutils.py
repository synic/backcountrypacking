from django import template

register = template.Library()

@register.filter('tablerows')
def tablerows(items, count):
    items = [i for i in items] # copy the array or queryset
    while True:
        row = []
        b = False
        for i in range(0, int(count)):
            try:
                row.append(items.pop())
            except IndexError:
                row.append(None)
                b = True
        yield row
        if b: break
