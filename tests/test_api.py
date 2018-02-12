from flask import url_for


class TestApi:
    def test_api_toto(self, client):
        res = client.get(url_for('api.toto'))
        assert res.status_code == 200
        assert 'toto' in res.data
