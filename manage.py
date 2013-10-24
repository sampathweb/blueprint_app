#!/usr/bin/env python
import os

from flask.ext.script import Manager, Server
from app import create_app, db

env = os.environ.get('APPNAME_ENV', 'dev')
app = create_app('app.settings.%sConfig' % env.capitalize(), env)
app.debug = True

manager = Manager(app)
manager.add_command("runserver", \
                    Server(use_debugger = True, use_reloader = True))

@manager.shell
def make_shell_context():
    """Creates a python REPL with several default imports in the context of the app"""
    return dict(app=app)

@manager.command
def createdb():
    """Creates a database with all of the tables defined in your Alchemy models"""
    db.create_all()

if __name__ == "__main__":
    manager.run()