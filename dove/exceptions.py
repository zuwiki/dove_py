class DoveException(Exception):
    message = 'An error has occured'

    def __str__(self):
        return self.message

class RestrictedAttributeException(DoveException):
    def __init__(self, attributename):
        self.message = 'Access to attribute "%s" is restricted' % (attributename)

class NoProviderException(DoveException):
    message = 'No provder defined'
