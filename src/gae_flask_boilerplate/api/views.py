from flask_restplus import Resource, fields


from . import api, ns

CLIENTS = {
    'client1': {'task': 'build an API'},
    'client2': {'task': '?????'},
    'client3': {'task': 'profit!'},
}

client = api.model('Client', {
    'task': fields.String(required=True, description='The task details')
})



def abort_if_todo_doesnt_exist(client_id):
    if client_id not in CLIENTS:
        api.abort(404, "Client {} doesn't exist".format(client_id))


parser = api.parser()
parser.add_argument('task', type=str, required=True, help='The task details', location='form')


@ns.route('/<string:client_id>')
@api.doc(responses={404: 'Todo not found'}, params={'client_id': 'The Client ID'})
class Client(Resource):
    """Show a single todo item and lets you delete them"""
    @api.doc(description='client_id should be in {0}'.format(', '.join(CLIENTS.keys())))
    @api.marshal_with(client)
    def get(self, client_id):
        """Fetch a given resource"""
        abort_if_todo_doesnt_exist(client_id)
        return CLIENTS[client_id]

    @api.doc(responses={204: 'Todo deleted'})
    def delete(self, client_id):
        """Delete a given resource"""
        abort_if_todo_doesnt_exist(client_id)
        del CLIENTS[client_id]
        return '', 204

    @api.doc(parser=parser)
    @api.marshal_with(client)
    def put(self, client_id):
        """Update a given resource"""
        args = parser.parse_args()
        task = {'task': args['task']}
        CLIENTS[client_id] = task
        return task
