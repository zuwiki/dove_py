Control Flow
============

Estimated structure of Dove. PLEASE change what you see here.

The server is divided into four sections:

  - The transport talks to the outside world (Does this really need to be separate from the handler? Obviously we want thread-safety, but is this division necessary even for that?)
  - The handler sends commands to the correct RPC modules
  - RPC modules do work
  - The repository keeps all the data

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

RPC Modules
-----------

These are regular Python modules stored in the `rpc` folder.

    Handle Call ( command, arguments ) ->
        Do whatever.

Repository
----------

*((This is probably a ways off. Not an essential feature. The whole `searchTasks()` thing would be a mite difficult.))*

Someone might have reason to use something other than SQL, so we should allow the use of whatever storage mechanism a server operator likes. It would also be good to allow the use of multiple storage devices. For instance, an OS X user might want their local server to integrate with iCal. That would lose data, so they wouldn't want to only use that for their storage. Therefore, they could have the repository save data to both a SQL database and iCal, then identify a primary device for retrieving data from (in this case, the SQL database).