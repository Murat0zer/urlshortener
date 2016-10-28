"""
<<<<<<< HEAD
WSGI config for urlshortener project.
=======
WSGI config for urlshorter project.
>>>>>>> a3935f5cb7149c5d45d3e0d931cc20de28a6e267

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "urlshortener.settings")

application = get_wsgi_application()
