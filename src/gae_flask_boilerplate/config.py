import os

basedir = os.path.abspath(os.path.dirname(__file__))

if os.environ.get('SERVER_SOFTWARE', '').startswith('Development') or os.environ.get('SERVER_SOFTWARE', '') == '':
    DEVELOPMENT = True
else:
    DEVELOPMENT = False



class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
