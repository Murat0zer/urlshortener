from django.db import models

# Create your models here.


class UrlShortener(models.Model):
    url = models.CharField(max_length=200, )

    def __str__(self):
        return str(self.url)
