from google.appengine.ext import ndb


class Client(ndb.Model):
    clientname = ndb.StringProperty()
