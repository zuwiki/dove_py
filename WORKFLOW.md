Workflow
========

Estimated structure of Dove. PLEASE change what you see here.


    `listener` at doveip:doveport ->
        Receives request, spawns `handler`

    `handler` waits for a client's first command. It requires authentication before it accepts any methods using @requires_user decorator. (Example: `user.create` wouldn't have `@requires_user`, but `task.create` does.)

    For every command handler recieves is sent to the RPC Handler which looks into the `rpc` directory (TODO: This is all wrong) for modules that inherit from the RPCClass and the methods in them for an available command index.

    There's got to be a way to live load/unload RPC modules. Like if a client wanted to use a google calendar module, he wouldn't have to restart the server. We'll work that out in the future as to how a user can own a personal server and not a public one like on dottru.


Handler
-------

    Receive Request ( command, arguments ) ->
        Split command by '.', search for registered handlers for command[0]

    Example:
        Receive Request ( self, "task.create", {"description":"Feed the cat before it starves."})
            command is split into ["task", "create"]. The registered RPC module "task" is called to handle "create".
            Task . Handle ( command[1], arguments ) ->
                Now it can either return a response, or raise a NotFound exception,
                which is handled and the appropriate template is generated appropriately.

TODO: More
