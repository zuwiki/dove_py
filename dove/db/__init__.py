from models import *

metadata.bind = 'sqlite:////tmp/dove.sqlite'
metadata.bind.echo = False

# TODO: Bug 5e0
setup_all(True)
