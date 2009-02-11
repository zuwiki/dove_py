from dove.protocol.rpc import DoveService, ServiceMethod

@ServiceMethod
def create(user={}):
    return 'Created user `rawr screw you!`'
 
@ServiceMethod
def update(user={}):
    return 'Updated user `rawr screw you!`'
 
@ServiceMethod
def delete(uid=None):
    return 'Deleted user `rawr screw you!`' 
