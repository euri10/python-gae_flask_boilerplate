from flask_restplus import Resource, fields
from google.appengine.ext import ndb

from . import api, ns




class Client(ndb.Model):
    clientname=ndb.StringProperty()

client = api.model('Client', {
    'clientname': fields.String,
})
parser = api.parser()
parser.add_argument('task', type=str, required=True, help='The task details', location='form')


@ns.route('/<string:client_id>')
@api.doc(responses={404: 'Todo not found'}, params={'client_id': 'The Client ID'})
class ClientResource(Resource):
    """Show a single todo item and lets you delete them"""
    @api.doc('get client')
    def get(self, client_id):
        """Fetch a given resource"""
        client = Client.get_by_id(client_id)
        return {'clientname': client.clientname}, 200

    @api.doc('create client')
    def post(self, client_id):
        """Create a new task"""
        clientname = api.payload.get('clientname')
        client = Client(id=clientname, clientname=clientname)
        client_key = client.put()
        return {'clientname': client.clientname}, 201
