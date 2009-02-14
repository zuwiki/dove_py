from models import *

metadata.bind = 'sqlite:////tmp/dove.sqlite'
metadata.bind.echo = False

# TODO: Bug 5e0
setup_all(True)

class RequiredFieldException(Exception):
    def __init__(self, field):
        self.field = field

    def __str__(self):
        return 'Missing required field "%s"' % (self.field)
