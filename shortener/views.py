from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from . models import UrlShortener
# Create your views here.


def url_redirect_fb_view(request, shortcode=None, *args, **kwargs):
    obj = get_object_or_404(UrlShortener, shortcode=shortcode)
    return HttpResponse("Hello {sc}".format(sc=obj_url))


class UrlREdirectCBView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(UrlShortener, shortcode=shortcode)
        return HttpResponse("Hello {sc}".format(sc=obj_url))
