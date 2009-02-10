import threading
import traceback

import simplejson as json

class Handler(object):

    def __init__(self):
        '''
        This is needed for a __call__ with a parameter.

        Without __init__ this error occurs.
        TypeError: default __new__ takes no parameters
        '''
        pass

    def __call__(self, jsonstring):
        '''
        Quick shortcut method to Handler.handle
        '''
        self.handle(jsonstring)

    def handle(self, jsonstring):
        '''
        Parse jsonstring into its corresponding module, method, and arguments,
        then pass it off appropriately. Then take whatever is returned and send
        it back to the client.
    
        Takes a valid JSON string like this:
            {"id":id, "method":"<module>.<method>", "params":params}
        '''
        print 'Got request "%s"' % (jsonstring)
        
        # TODO: Better error handling
        # BUG: 285
        try:
            request = self.parse(jsonstring)
            module = __import__('dove.modules.'+request['module'], fromlist=[request['method']])
            method = module.__dict__[request['method']]
            retval = method(request['params'])

            return json.dumps({'id': request['id'], 'result': retval})

        except ValueError:
            return json.dumps({'id': None, 'error': 'Invalid request.'})


    def parse(self, jsonstring):
        '''
        Parses a json string into callid, module, method, and arguments,

        Takes a valid JSON string like this:
            {"id":id, "method":"<module>.<method>", "params":params}
        '''
        requeststring = json.loads(jsonstring)
        callid = requeststring['id']
        module, method = requeststring['method'].split('.')
        params = requeststring['params']
        return {'id':callid, 'module':module,
               'method':method, 'params':params}
        return requeststring
