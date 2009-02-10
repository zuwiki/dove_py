from dove.protocol.rpc import DoveService, ServiceMethod

@ServiceMethod
def create(self, user={}):
    return 'Created user `rawr screw you!`'
 
@ServiceMethod
def update(self, user={}):
    return 'Updated user `rawr screw you!`'
 
@ServiceMethod
def delete(self, uid=None):
    return 'Deleted user `rawr screw you!`' 
