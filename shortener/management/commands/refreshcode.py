from django.core.management.base import BaseCommand, CommandError
from shortener.models import UrlShortener


class Command(BaseCommand):
    help = 'Refreshing shortcode of urls'

    def add_arguments(self, parser):
        parser.add_argument('items', type=int)

    def handle(self, *args, **options):
        return UrlShortener.objects.refresh_shortcodes(items=options['items'])
