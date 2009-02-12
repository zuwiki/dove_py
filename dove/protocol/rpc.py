import simplejson as json

class RPCRequest(object):
    '''
    A generic class to represent a JSON-RPC request
    '''
    id = None
    module = None
    method = None
    params = None

    def __init__(self, id=None, module = None, method=None, params=None, jsonstring=None):

        if jsonstring:
            request = json.loads(jsonstring)

            print "RAWR MY REQUEST %s" % (request)

            if 'id' in request: self.id = request['id']
            if 'params' in request: self.params = request['params']

            if 'method' in request:
                self.module, self.method = request['method'].split('.')
        
        print self

        if id: self.id = id
        if module: self.module = module
        if method: self.method = method
        if params: self.params = params

        print self

    def __str__(self):
        return json.dumps({'id':self.id, 'method': self.module+'.'+self.method, 'params': self.params})
   

class RPCResponse(object):
    '''
    A generic class to represent a JSON-RPC response
    '''
    id = None
    result = None
    error = None

    def __init__(self, id=None, result=None, error=None, jsonstring=None):

        if jsonstring:
            request = json.loads(jsonstring)
        
            if 'id' in request: self.id = request['id']
            if 'result' in request: self.result = request['result']
            if 'error' in request: self.error = request['error']

        if id: self.id = id
        if result: self.result = result
        if error: self.error = error

    def __str__(self):
        return json.dumps({'id':self.id, 'result': self.result, 'error': self.error})

class InvalidRequestError(RPCResponse):
    error = "JSON-RPC request was invalid."

class EmptyRequestError(RPCResponse):
    error = "Empty request."
