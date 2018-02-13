import json

import pytest
from flask.testing import FlaskClient

from gae_flask_boilerplate import create_app


class TestClient(FlaskClient):
    def get_json(self, url, status=200, **kwargs):
        response = self.get(url, **kwargs)
        assert response.status_code == status
        assert response.content_type == 'application/json'
        return json.loads(response.data.decode('utf8'))

    def post_json(self, url, data, status=200, **kwargs):
        response = self.post(url, data=json.dumps(data),
                             headers={'content-type': 'application/json'}, **kwargs)
        assert response.status_code == status
        assert response.content_type == 'application/json'
        return json.loads(response.data.decode('utf8'))

    def get_specs(self, prefix='', status=200, **kwargs):
        """Get a Swagger specification for a RestPlus API"""
        return self.get_json('{0}/swagger.json'.format(prefix), status=status, **kwargs)


@pytest.fixture
def app():
    app = create_app('testing')
    app.test_client_class = TestClient
    yield app


# @pytest.fixture(autouse=True)
# def _push_custom_request_context(request):
#     app = request.getfuncargvalue('app')
#     options = request.keywords.get('request_context')
#
#     if options is None:
#         return
#
#     ctx = app.test_request_context(*options.args, **options.kwargs)
#     ctx.push()
#
#     def teardown():
#         ctx.pop()
#
#     request.addfinalizer(teardown)
