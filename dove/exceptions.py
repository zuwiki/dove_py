class DoveException(Exception):
    message = 'An error has occured'

    def __str__(self):
        return self.message

class RestrictedAttributeException(DoveException):
    def __init__(self, attributename):
        self.message = 'Access to attribute "%s" is restricted' % (attributename)

class NoProviderException(DoveException):
    message = 'No provider defined'

class RequiredFieldException(DoveException):
    def __init__(self, field):
        self.message = 'Missing required field "%s"' % (field)

class InvalidURIException(DoveException):
    def __init__(self, uri):
        self.message = 'The URI "%s" is invalid' % (uri)
