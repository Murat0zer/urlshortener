from django.db import models
from .utils import code_generator, create_shortcode
# Create your models here.


class UrlShortenerUrlManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(UrlShortenerUrlManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcodes(self):
        qs = UrlShortener.objects.filter(id__gte=1)
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.shortcode)
            q.save()
            new_codes += 1
        return "New codes made: {i}".format(i=new_codes)

class UrlShortener(models.Model):
    url = models.CharField(max_length=200, )
    shortcode = models.CharField(max_length=20, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = UrlShortenerUrlManager()
    some_random = UrlShortenerUrlManager()

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(UrlShortener, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
