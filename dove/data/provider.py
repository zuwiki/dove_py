from dove.exceptions import *
from couchdb.client import Server

class CouchProvider(object):
    def __init__(self, uri=None, database=None):
        print '%s|%s' % (uri, database)
        self.server = Server(uri)

        try:
            # python-couchdb will create the database or raise an error if it
            # already exists
            self.database = self.server.create(database)
        except:
            self.database = self.server[database]

    def fetch(self, uuid, type=None):
        doc = self.database[uuid]
        if doc['type'] == type:
            return doc
        else:
            raise DocumentNotFoundException(uuid)


