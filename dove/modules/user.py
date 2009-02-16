import uuid

from dove.db import *

def create(user={}):
    '''
    Saves a new user to the database.
    '''
    
    # Check to see if this is worth saving
    validate_user(user)

    # Create a user and generate a new uuid
    u = User(**user)
    u.uuid = uuid.uuid1().__str__()

    return {'message': 'Created user %s' % (u.uuid), 'uuid': u.uuid}
 
def update(user={}):
    '''
    Updates an existing user in the database
    '''
    
    # Check for a uuid, this is what we use to find a user
    if not 'uuid' in user.keys():
        raise RequiredFieldException('uuid')

    # Find a single user that matches this. Will error out if a problem happens
    u = User.query.filter_by(uuid=user['uuid']).one()

    # Loop through and set the new data
    for key in user.keys():
        u.__setattr__(key, user[key])
    
    return {'message': 'Updated user %s' % (u.uuid), 'uuid': u.uuid}
 
def delete(uuid=None):
    User.delete(User.query.filter_by(uuid=uuid).one())
    return {'message': 'Deleted user %s' % (uuid), 'uuid': u.uuid}


def validate_user(user):
    '''
    Validates a user object

    returns bool
    '''
    # TODO: Bug ab1

    for required in ('email', 'password'):
        if not required in user.keys():
            raise RequiredFieldException(required)
