from django.db import models
from sorl.thumbnail import ImageField


class Image(models.Model):
    image = ImageField(upload_to="dcimages/%Y/%m/%d")
    name = models.SlugField(blank=True, null=True, unique=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    package = models.ForeignKey(
        'dropcamp.Package',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return "%s - %s" % (self.name, self.image.url)


class Page(models.Model):
    url = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    large_image = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        related_name='page_set1',
        on_delete=models.SET_NULL,
    )
    small_image_1 = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        related_name='page_set2',
        on_delete=models.SET_NULL,
    )
    small_image_2 = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        related_name='page_set3',
        on_delete=models.SET_NULL,
    )
    small_image_3 = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        related_name='page_set4',
        on_delete=models.SET_NULL,
    )
    text = models.TextField()

    def __str__(self):
        return self.url


class Package(models.Model):
    TYPES = (
        ('area', 'Area'),
        ('package', 'Package'),
    )

    name = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(max_length=40, unique=True)
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=15, choices=TYPES)
    description = models.TextField()
    price = models.FloatField(default=0.0)

    @property
    def first_image(self):
        try:
            return self.image_set.order_by('id')[0]
        except IndexError:
            return None

    def __str__(self):
        return self.name


class Link(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200, null=True, blank=True)
    url = models.CharField(max_length=255)
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.name
