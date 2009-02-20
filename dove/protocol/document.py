from dove.exceptions import *
import simplejson as json

class Document(object):
    '''
    The base data storage container
    '''
    data = {}
    restricted = ['type']
    provider = None

    def __setattr__(self, name, value):
        if name not in self.restricted:
            self.__dict__[name] = value
        else:
            raise RestrictedAttributeException(name)

    def __getattr__(self, name):
        return self.__dict__[name]

    def json(self):
        return json.dumps(self.__dict__)

    def save(self):
        if self.provider:
            self.provider.save(self.json())
        else:
            raise NoProviderException()
