#! ../env/bin/python
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(object_name, env):
    """
    An flask application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/

    Arguments:
        object_name: the python path of the config object,
                     e.g. appname.settings.ProdConfig

        env: The name of the current environment, e.g. prod or dev
    """
    app = Flask(__name__)

    app.config.from_object(object_name)
    app.config['ENV'] = env

    #init SQLAlchemy
    db.init_app(app)

    # Register Blueprints
    from tasks.views import tasks
    app.register_blueprint(tasks)

    from main.views import main
    app.register_blueprint(main)

    return app