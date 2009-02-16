from models import *

# TODO: Bug d47
metadata.bind = 'sqlite:////tmp/dove.sqlite'
metadata.bind.echo = False

setup_all(True)

# TODO: Bug 2a7
class RequiredFieldException(Exception):
    def __init__(self, field):
        self.field = field

    def __str__(self):
        return 'Missing required field "%s"' % (self.field)
