from flask import url_for


class TestApi:
    def test_api_client_url_for(self, app):
        with app.test_request_context():
            url = url_for('api.clients_client', client_id='client1')
            assert url == '/api/1/clients/client1'
            with app.test_client() as client:
                res = client.get_json(url)
                assert res == {'task': 'build an API'}
