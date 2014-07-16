# coding: utf-8

"""
WSGI config for demoApp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""


# make wsgi load application path
import sys
sys.path.append('/cygdrive/c/Users/scott.lan/workspace/for_ssd/wsgi_study/demoApp/')  # noqa
sys.path.append('/home/scott.lan/ssd_server/.venv/lib/python2.7/site-packages')  # noqa

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demoApp.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()



# 或許可以拿來替換 Django 的 WSGI Application
from wsgiref.simple_server import make_server
httpd = make_server('127.0.0.1', 5555, application)
httpd.serve_forever()
