import sys
import os

APPNAME="basic_app"
URLPATH = "/basic"
HOMEDIR = "rsam"

sys.path.insert(0, '/home/' + HOMEDIR + '/webapps/' + APPNAME + '/' + APPNAME)
activate_this = '/home/' + HOMEDIR + '/webapps/' + APPNAME + '/' + APPNAME + '/env/bin/activate_this.py'
execfile(activate_this, {"__file__": activate_this})

from app import app

class WebFactionMiddleware(object):
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response):
        environ['SCRIPT_NAME'] = URLPATH
        return self.app(environ, start_response)

app.wsgi_app = WebFactionMiddleware(app.wsgi_app)

application = app
