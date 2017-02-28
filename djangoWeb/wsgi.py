"""
WSGI config for djangoWeb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os,sys
from os.path import join,dirname,abspath

os.environ["DJANGO_SETTINGS_MODULE"] = "djangoWeb.settings"

sys.path.append('/var/DjangoWeb/venv/lib/python3.5/site-packages')

PROJECT_DIR = dirname(dirname(abspath(__file__)))
if PROJECT_DIR not in sys.path:
	sys.path.insert(0,PROJECT_DIR)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
