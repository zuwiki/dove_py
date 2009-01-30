from elixir import *

class User(Entity):
    uid             = Field(String(40)) # sha of the time when user was created
    email           = Field(String(320), required=True) # http://tinyurl.com/2sl2uv
    fullname        = Field(Unicode(30)) # Arbitrary length
    password        = Field(String(40), required=True) # SHA password + hash
    salt            = Field(Unicode(16))
    tasks           = OneToMany('Task')
    tagtree         = Field(PickleType, deferred=True) # Abstain from pulling on every query

    def __repr__(self):
        return "<User '%s'>" % (self.email)

class Task(Entity):
    uid             = Field(String(32)) # sha of the time when task was created
    description     = Field(Unicode(128), required=True) # A short description
    details         = Field(Text, deferred=True) # Abstain from pulling on every query
    complete        = Field(Boolean)

    start_date      = Field(DateTime)
    end_date        = Field(DateTime)

    owner           = ManyToOne('User', required=True) # User
    tags            = ManyToMany('Tag')

    lastmodified    = Field(DateTime)

    def __repr__(self):
        return "<Task '%s'>" % (self.uid[:8]) # First eight characters of the UID

class Tag(Entity):
    name = Field(Unicode(255), primary_key=True)
    tasks = ManyToMany('Task')
