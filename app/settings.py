import os

class Config(object):
    #common config
    pass

class ProdConfig(Config):
    SECRET_KEY = 'prod - tis is secret?'
    # SQL Alchemy settings
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/app_prod.sqlite'

class DevConfig(Config):
    SECRET_KEY = 'dev tis is secret?'
    DEBUG = True
    # SQL Alchemy settings
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/app_dev.sqlite'
    SQLALCHEMY_ECHO = True
