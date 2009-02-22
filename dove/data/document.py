from dove.exceptions import *
from dove.data.provider import *
import simplejson as json
from uuid import uuid1 as gen_uuid

class Document(object):
    '''
    The base data storage container
    '''
    provider = None

    provider = CouchProvider('http://localhost:5984/', 'dove')

    def __init__(self, uuid=None):
        # Set the type to the name of the class.
        self.__dict__['type'] = self.__class__.__name__.lower()
        # If there is a uuid, instantiate it.
        if uuid:
            self.get(uuid)
        # Otherwise, generate a uuid - our ojbect is new.
        else:
            self._id = gen_uuid().__str__()

    def get(self, uuid):
        doc = self.provider.fetch(uuid, self.type)
        for key in doc:
            self.__setattr__(key, doc[key])

    def __setattr__(self, name, value):
        self.__dict__[name] = value

    def __getattr__(self, name):
        return self.__dict__[name]

    def json(self):
        return json.dumps(self.__dict__)

    def save(self):
        if self.provider:
            self.provider.save(self.json())
        else:
            raise NoProviderException()

    def __repr__(self):
        return '<%s %s>' % (self.__class__.__name__, self._id)
