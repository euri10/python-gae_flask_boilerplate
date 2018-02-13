from flask import url_for


class TestApi:
    def test_api_client_url_for(self, app):
        clientname = 'totoclient'
        with app.test_request_context():
            url = url_for('api.clients_client_resource', client_id=clientname)
            assert url
            with app.test_client() as client:
                data = {'clientname': clientname}
                res = client.post_json(url, data, status=201)
                assert res == data
                res = client.get_json(url)
                assert res == data
