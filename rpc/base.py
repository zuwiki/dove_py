class RPCClass(object):
    '''
    RPC Base Class

    The base class all RPC classes inherit from.
    '''
    pass


def RPCMethod(func):
    '''
    A decorator to let the RPC Class know which methods are
    RPC methods or just internal
    '''
    func.IsRPCMethod = True
    return func
