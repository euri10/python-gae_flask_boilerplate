import json
import os
import sys

import pytest
from flask.testing import FlaskClient

from gae_flask_boilerplate import create_app

sys.path.insert(1, '/home/lotso/google-cloud-sdk/platform/google_appengine')
sys.path.insert(1, '/home/lotso/PycharmProjects/python-gae_flask_boilerplate/src/gae_flask_boilerplate')
import dev_appserver  # noqa:E402 isort:skip


dev_appserver.fix_sys_path()  # isort:skip
from google.appengine.tools.devappserver2 import application_configuration  # noqa:E402 isort:skip


cfg = application_configuration.ApplicationConfiguration(['/home/lotso/PycharmProjects/python-gae_flask_boilerplate/src/gae_flask_boilerplate/app.yaml'])  # noqa:E501
os.environ['APPLICATION_ID'] = cfg.app_id
# simulate same environment as devappserver2
os.environ['CURRENT_VERSION_ID'] = cfg.modules[0].version_id


try:
    import appengine_config  # noqa:F401
except ImportError:
    print('Note: unable to import appengine_config.')

from google.appengine.ext import testbed  # noqa:E402 isort:skip


@pytest.fixture(autouse=True)
def tb():
    tb = testbed.Testbed()
    # Then activate the testbed, which will allow you to use
    # service stubs.
    tb.activate()
    # Next, declare which service stubs you want to use.
    tb.init_datastore_v3_stub()
    tb.init_memcache_stub()
    # tb.init_user_stub()
    yield tb
    # Don't forget to deactivate the testbed after the tests are
    # completed. If the testbed is not deactivated, the original
    # stubs will not be restored.
    tb.deactivate()


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
