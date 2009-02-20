import uuid

from dove.db import *

def create(task={}):
    '''
    Saves a new task to the database.
    '''
    
    # Check to see if this is worth saving
    validate_task(task)

    # TODO: Bug a4b
    task['owner'] = User.query.filter_by(uuid=task['owner']).one()

    # Create a task and generate a new uuid
    t = Task(**task)
    t.uuid = uuid.uuid1().__str__()

    return {'message': 'Created task %s' % (t.uuid), 'uuid': t.uuid}
 
def update(task={}):
    '''
    Updates an existing task in the database
    '''
    
    # Check for a uuid, this is what we use to find a task
    if not 'uuid' in task.keys():
        raise RequiredFieldException('uuid')

    # Find a single task that matches this. Will error out if a problem happens
    t = Task.query.filter_by(uuid=task['uuid']).one()

    # Loop through and set the new data
    for key in task.keys():
        t.__setattr__(key, task[key])
    
    return {'message': 'Updated task %s' % (t.uuid), 'uuid': t.uuid}
 
def delete(uuid=None):
    Task.delete(Task.query.filter_by(uuid=uuid).one())
    return {'message': 'Deleted task %s' % (uuid), 'uuid': t.uuid}

def get(uuid=None):
    t = Task.query.filter_by(uuid=uuid).one()
    return {'task': t.to_dict()}


def validate_task(task):
    '''
    Validates a task dict
    '''

    for required in ('owner', 'description'):
        if not required in task.keys():
            raise RequiredFieldException(required)
