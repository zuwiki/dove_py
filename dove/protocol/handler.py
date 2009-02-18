import threading
import traceback

from dove.protocol.rpc import *
from dove.db import *

class Handler(object):

    def __init__(self):
        '''
        This is needed for a __call__ with a parameter.

        Without __init__ this error occurs.
        TypeError: default __new__ takes no parameters
        '''
        pass

    def __call__(self, jsonstring, transport=None):
        '''
        Quick shortcut method to Handler.handle
        '''
        return self.handle(jsonstring, transport)

    def handle(self, jsonstring, transport=None):
        '''
        Pass off request to it's module/method appropriately. Then
        take whatever is returned and send it back to the client.
    
        Takes a valid JSON string like this:
            {"id":id, "method":"<module>.<method>", "params":params}
        '''
        # TODO: Bug 703
        print 'Got request "%s"' % (jsonstring) # TODO: Bug 8d2
        

        if not jsonstring: return EmptyRequestError()

        try:
            request = RPCRequest(jsonstring=jsonstring)
            # TODO: Bug 285, Bug 560
            module = __import__('dove.modules.'+request.module, fromlist=[request.method])

            # TODO: Bug 20b
            module = reload(module)

            method = module.__dict__[request.method]
            
            try:
                if request.params:
                    retval = method(request.params)
                else:
                    retval = method()
            except Exception, (instance):
                return RequestError(instance)

            session.commit() # Save any changes to the database

            return RPCResponse(id=request.id, result=retval)

        except ValueError:
            return InvalidRequestError()
