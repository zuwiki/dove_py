Workflow
========

Estimated structure of Dove. PLEASE change what you see here.

The Transport is the mechanism that dove sends and receives JSON-RPC calls (calls is redundant here). It simply listens at a specified address and dispatches off calls to a handler. For now, `transport` is for stream connections only. In the future it *should* be expanded to allow for an HTTP transport or other to-be-determined protocols.

The Handler waits for a client's first command. For every command handler recieves is sent to the RPC Handler which looks into the `rpc` directory (TODO: This is all wrong) for modules that inherit from the RPCClass and the methods in them for an available command
index.


There needs to be a way to live load/unload RPC modules. Imagine, a client wanted to use a google calendar module, he wouldn't have to restart the server. We'll work that out in the future as to how a user can own a personal server and not a public one like on dottru.

Transport
---------

    `transport` at doveip:doveport ->
        Receives request, dispatch to new `handler` thread

Handler
-------

    Receive Request ( jsonstring ) ->
        Parse jsonstring into its corresponding object. catch exceptions and
        return them as errors in this process.

        Run Handle Request ( jsonstring['command'], jsonstring['arguments'])


    Handle Request ( command, arguments ) ->
        Split command by '.', search for registered handlers for command[0]

    Example:
        Handle Request ( "task.create", {"description":"Feed the cat before it starves."})
            command is split into ["task", "create"]. The registered RPC module "task" is called to handle "create".
            Task . Handle ( command[1], arguments ) ->
                Now it can either return a response, or raise a NotFound exception,
                which is handled and the appropriate template is generated appropriately.
