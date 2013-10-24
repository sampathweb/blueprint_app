#!/usr/bin/env python
import os
from flask.ext.script import Manager, Server
from app import app, db

manager = Manager(app)
manager.add_command("runserver", \
                    Server(use_debugger = True, use_reloader = True, port=5000))
app.debug = True
app.config['SQLALCHEMY_ECHO'] = True

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