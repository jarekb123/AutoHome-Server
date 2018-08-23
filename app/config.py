import os


class Config(object):
    """ Base configuration class """
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = 'jfdsoifj3409rjk9jdg09q-r0mfxziov-2342--0f-3qrfxmzo=4242153'

    DB_USERNAME = 'root'
    DB_PASSWORD = ''
    DB_NAME = 'auto_home'
    DB_HOST = os.getenv('IP', '127.0.0.1')
    DB_URI = "mysql+pymsql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME)

    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """ Development app configuration class """
    DEBUG = True


class TestingConfig(Config):
    """ Configurations for Testing, with a separate test db """
    TESTING = True
    DB_NAME = 'test_auto_home'
    DEBUG = True


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig
}
