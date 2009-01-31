Control Flow
============

Estimated structure of Dove. PLEASE change what you see here.

The server is divided into four sections:

  - The transport talks to the outside world (Does this really need to be separate from the handler? Obviously we want thread-safety, but is this division necessary even for that?)
  - The handler sends commands to the correct RPC modules
  - RPC modules do work
  - The store keeps all the data

In the future, this will allow for the different parts to be swapped in and out at will. For example, you may want the store to use SQL, CouchDB, FS/YAML, or whatever. Maybe even Google Calendar. And of course being able to swap around RPC modules will allow extended functionality.

*((You know what I love? When I'm writing software and realize I could extract a damn nifty framework from it.))*

Transport
---------

    `transport` at doveip:doveport ->
        Receives request, dispatches to new `handler` thread

Handler
-------

    Receive Request ( jsonstring ) ->
        Parse jsonstring into its corresponding object. Catch exceptions and
        return them as errors in this process.

        Run Handle Request ( jsonstring['command'], jsonstring['arguments'])


    Handle Request ( command, arguments ) ->
        Split command by '.', search for registered handlers for command[0]

    Example:
        Handle Request ( "task.create", {"description":"Feed the cat before it starves."})
            Command is split into ["task", "create"]. The registered RPC module "task" is called to handle "create".
            Task . Handle ( command[1], arguments ) ->
                Now it can either return a response, or raise a NotFound exception,
                which is handled and the appropriate template is generated.
