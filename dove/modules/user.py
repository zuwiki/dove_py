from dove.modules.base import RPCClass, RPCMethod

class user(RPCClass):

    @RPCMethod
    def create(self, userdict):
        pass

    @RPCMethod
    def update(self, userdict):
        pass

    def delete(self, uid):
        pass
