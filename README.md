# How to start

    python wsgi_server.py


# use Django project_name/wsgi.py as Sample

    # make Apache WSGI can Load .venv site-packages
    import sys

    # make wsgi load application path
    sys.path.append('/home/scott.lan/ssd_server/')  # noqa
    sys.path.append('/home/scott.lan/ssd_server/.venv/lib/python2.7/site-packages')  # noqa

    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ssd_server.settings")

    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()


    # add my wsgi launch code here...
    from wsgiref.simple_server import make_server

    # 或許可以拿來替換 Django 的 WSGI Application
    httpd = make_server(
        '127.0.0.1', 5555, application)

    httpd.serve_forever()
