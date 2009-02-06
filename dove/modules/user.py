from dove.protocol.rpc import DoveService, ServiceMethod
 
class user(DoveService):
 
    @ServiceMethod
    def create(self, user={}):
        pass
 
    @ServiceMethod
    def update(self, user={}):
        pass
 
    @ServiceMethod
    def delete(self, uid=None):
        pass
