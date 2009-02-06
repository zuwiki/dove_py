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
            {"id":id, "method":"<module>.<method>", "params":params]
        '''
        request = parse(jsonstring)
        module = __import__(request['module'])
        method = __dict__[request['method']]
        retval = method(request['params'])
        return json.dumps({'callid'})
        

    def parse(jsonstring):
        '''
        Parses a json string into callid, module, method, and arguments,
    
        Takes a valid JSON string like ["callid", "module.method", arguments]
        '''
        requeststring = json.loads(jsonstring)
        callid = requeststring[0]
        module, method = requeststring[1].split(".")
        arguments = requeststring[2]
        return {'callid':callid, 'module':module,
                'method':method, 'arguments':arguments}
