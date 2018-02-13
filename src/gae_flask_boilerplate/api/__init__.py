from flask import Blueprint
from flask_restplus import Api

api_v1 = Blueprint('api', __name__, url_prefix='/api/1')
api = Api(api_v1, version='1.0', title='Client API', description='A simple Client API')

ns = api.namespace('clients', description='clients operations')


from . import views  # noqa:E402,F401 isort:skip
