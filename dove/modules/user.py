from dove.protocol.rpc import DoveService, ServiceMethod

class user(DoveService):

    @ServiceMethod
    def create(self, userdict={}):
        pass

    @ServiceMethod
    def update(self, userdict={}):
        pass

    @ServiceMethod
    def delete(self, uid=None):
        pass
