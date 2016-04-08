#coding:utf-8


from gevent import monkey
monkey.patch_all()
from gevent.wsgi import WSGIServer
from django_web.wsgi import application
from django_web.settings import BASE_DIR
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_web.settings")

from werkzeug.serving import run_with_reloader
@run_with_reloader
def run_server():
    http_server = WSGIServer(('0.0.0.0', 9999), application)
    http_server.serve_forever()