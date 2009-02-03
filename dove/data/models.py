from elixir import *

class User(Entity):
    '''
    Dove user entity

    Represents a user on Dove, required fields are email and password.
    (Bare minimum to login) Everything else is optional.
    '''

    # The User's unique identifier is used to specify a precise user in Dove.
    # Each uid is generated upon creation as an SHA hash of the current unix
    # timestamp.
    # TODO: Actually generate this, and use a UUID not a SHA hash
    uid             = Field(String(40))

    # A User's email address is that user's human-readable identifier, required.
    # Also functions as a login username and a contact address.
    # For maximum length, see http://tinyurl.com/2sl2uv
    email           = Field(String(320), required=True)

    # User's full name, used for interface greetings, etc.
    fullname        = Field(Unicode(30))

    # User's password is an SHA hash of the password + salt, required
    password        = Field(String(40), required=True)
    salt            = Field(String(16))

    # User tasks are a One-To-Many relationship to Task objects
    tasks           = OneToMany('Task')
    
    # The User Tag Tree is a pickle of a dict Tag Tree
    # (The `deferred=True` here means that this collumn won't be pulled automatically)
    tagtree         = Field(PickleType, deferred=True)

    def __repr__(self):
        '''
        Object Representation

        Example output:
            <User 'test@doveproject.net'>
        '''
        return "<User '%s'>" % (self.email)


class Task(Entity):
    '''
    Dove task entity

    Represents a task on Dove, requires a description and an owner. All
    other fields are optional.
    '''

    # The User's unique identifier is used to specify a precise user in Dove.
    # Each uid is generated upon creation as an SHA hash of the current unix
    # timestamp.
    # TODO: Actually generate this, and use a UUID not a SHA hash
    uid             = Field(String(32))

    # A short text description of this task, required.
    description     = Field(Unicode(128), required=True)

    # A (probably unused) column for clients to store additional information.
    details         = Field(Text, deferred=True)

    # Whether or not this task has been finished.
    complete        = Field(Boolean)

    # The beginning and end date for this task
    start_date      = Field(DateTime)
    end_date        = Field(DateTime)

    # An owner is the user who created this task
    owner           = ManyToOne('User', required=True)

    # A Many-To-Many relationship to tag objects
    tags            = ManyToMany('Tag')
    
    # Defaults to the last time this task was modified (for synchronization)
    lastmodified    = Field(DateTime)

    def __repr__(self):
        '''
        Task Representation

        Example output:
            <Task 'de9f2c7f'>
        '''
        return "<Task '%s'>" % (self.uid[:8]) # First eight characters of the UID

class Tag(Entity):
    '''
    Dove tag entity

    Represents a tag, will probably be phased out for a better alternative
    '''
    name = Field(Unicode(255), primary_key=True)
    tasks = ManyToMany('Task')
