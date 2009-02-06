import threading
import simplejson as json

class Handler(object):
    def __init__(self):
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
        request = self.parse(jsonstring)
        module = __import__(request['module'], fromlist=['modules'])
        method = module.__dict__[request['method']]
        retval = method(request['params'])
        return json.dumps({'id': request['id'], 'result': retval})

    def parse(self, jsonstring):
        '''
        Parses a json string into callid, module, method, and arguments,

        Takes a valid JSON string like this:
            {"id":id, "method":"<module>.<method>", "params":params}
        '''
        requeststring = json.loads(jsonstring)
        callid = requeststring['id']
        module, method = requeststring['method'].split(".")
        params = requeststring['params']
        return {'id':callid, 'module':module,
               'method':method, 'params':params}
        return requeststring
