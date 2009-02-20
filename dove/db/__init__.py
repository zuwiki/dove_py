from models import *

# TODO: Bug d47
metadata.bind = 'sqlite:////tmp/dove.sqlite'
metadata.bind.echo = False

setup_all(True)
