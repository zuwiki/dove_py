import simplejson as json

class Handler:
    def __init__(self):
        pass

    def handle(self, jsonstring):
        '''
        Parse jsonstring into its corresponding module, method, and arguments,
        then pass it off appropriately. Then take whatever is returned and send
        it back to the client.
    
        Takes a valid JSON string like ["callid", "module.method", arguments]
        '''
        request = parse(jsonstring)
        module = __import__(request['module'])

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