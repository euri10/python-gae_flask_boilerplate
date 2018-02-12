__version__ = '0.1.0'


from config import config
from flask import Flask


def create_app(config_name):
    """Application factory, used to create application
    """
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')
    return app
