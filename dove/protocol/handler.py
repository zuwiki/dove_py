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
        return self.handle(jsonstring)

    def handle(self, jsonstring):
        '''
        Parse jsonstring into its corresponding module, method, and arguments,
        then pass it off appropriately. Then take whatever is returned and send
        it back to the client.
    
        Takes a valid JSON string like this:
            {"id":id, "method":"<module>.<method>", "params":params}
        '''
        print 'Got request "%s"' % (jsonstring) # TODO: Bug 8d2
        
        # TODO: Bug 285
        try:
            request = self.parse(jsonstring)
            # TODO: Bug 343
            module = __import__('dove.modules.'+request['module'], fromlist=[request['method']])
            method = module.__dict__[request['method']]
            if request.has_key('params'):
                retval = method(request['params'])
            else:
                retval = method()

            return json.dumps({'id': request['id'], 'result': retval})

        except ValueError:
            return json.dumps({'id': None, 'error': 'Invalid request.'})


    def parse(self, jsonstring):
        '''
        Parses a json string into callid, module, method, and arguments,

        Takes a valid JSON string like this:
            {"method":"<module>.<method>"}
        
        And returns a Python dictionary like this:
            {"method":method, "module":module}

        Any other elements present in the input will be preserved in the output.

        Note that the input must have exactly one top-level container:
        a dictionary, or in JSON lingo, an object.
        '''
        request = json.loads(jsonstring)
        module, method = request['method'].split('.')
        request['module'] = module
        request['method'] = method
        return request
