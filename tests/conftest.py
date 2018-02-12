import pytest

from gae_flask_boilerplate import create_app


@pytest.fixture
def app():
    app = create_app('testing')
    return app
