from flask_restplus import Resource, fields
from google.appengine.ext import ndb

from . import api, ns


class Client(ndb.Model):
    clientname = ndb.StringProperty()


client = api.model('ClientResource', {
    'clientname': fields.String,
})


@ns.route('/<string:client_id>')
@api.doc()
class ClientResource(Resource):
    """Show a single todo item and lets you delete them"""
    @api.doc('get client')
    @api.marshal_with(client)
    def get(self, client_id):
        """Fetch a given resource"""
        client = Client.get_by_id(client_id)
        if client is not None:
            return {'clientname': client.clientname}, 200
        else:
            return {'error': client_id}, 404

    @api.doc('create client')
    def post(self, client_id):
        """Create a new task"""
        clientname = api.payload.get('clientname')
        client = Client(id=clientname, clientname=clientname)
        client.put()
        return {'clientname': client.clientname}, 201
