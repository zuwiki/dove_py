#!/usr/bin/env python

from models import *

if __name__ == '__main__':

    # DB setup / initialization
    print('Initializing SQLite DB.')
    metadata.bind = 'sqlite:///' # Create a table in memory
    metadata.bind.echo = False

    setup_all(True)

    # DB save / query
    print('Creating a User and a Task.')
    u = User(uid="12345", email="test@doveproject.net", password="")
    t = Task(uid="45774", description=u'Send some test data over to support.', owner=u)

    print('Saving test User/Task to the DB.')
    session.commit()

    print('Querying for all Users...')
    users = User.query.all()
    print(users)

    print('Querying for all Tasks...')
    print(Task.query.all())

    print('Finding count of tasks for first user.')
    print(len(users[0].tasks))
