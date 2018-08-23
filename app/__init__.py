from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy

from app.config import app_config

db = SQLAlchemy()


def create_app(config_name):
    """ Creates Flask object with configuration
        :param config_name Name of the configuration set
    """
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    db.init_app(app)
    return app
