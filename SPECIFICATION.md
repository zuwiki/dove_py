Data
====

Here are the data models, they are represented in the system as JSON objects.

Tasks
-----

  - `id`* A unique task identifier
  - `description`* A short description
  - `details` Further task details, possibly a document stored as Base64
  - `completed` Whether or not the task has been completed
  - `start` When the task begins.
  - `due` When the task is due
  - `tags` A list of strings each representing a tag
  - `owner` Single user id of the creator
  - `participators` A list of ids for users allowed to see and edit the task
  - `lastmodified` Date and time of the task's last change

Required fields are noted with an asterisk. The `id` is generated for you and returned upon task creation. The field `completed` defaults to `False`. The field `owner` is defaulted to your user.id.

Users
-----

  - `id` A unique user identifier
  - `email` The user's contact email address
  - `password` A salted hash of the user's password
  - `salt` A salt for the user's password
  - `fullname` The users's IRL full name
  - `tagtree` see [Tag Tree]

Tag Tree
--------

A tag tree is a dict of tags belonging to a user. This is used on the client-side mostly. Tags used in a user's task are *not* required to be in the user's tag tree, but it assists in the categorization of tasks.

Example tag tree.

    {
        "home": {
            "chores": {
                "laundry": {},
                "dishes: {}
            }
        },
        "work": {
            "programming": {
                "c#": {
                    "weathermonitor": {},
                }
            },
            "refactor": {},
            "chores": {}
        },
        "art": {
            "music": {
                "guitar": {}
                "keyboard": {}
            },
            "programming": {
                "python": {},
                "erlang": {}
            }
        }
    }

TODO: Rework this, explain beter. Figure out resolution of home.chores vs work.chores or work.programming vs, art.programming.

Tag Tree
--------

TODO: Describe.

Dates
-----

Dates are encoded as text using the ISO 8601 format. More information is available on the [WWW Consortium website](http://www.w3.org/TR/NOTE-datetime "Date and Time Formats"), and an example is available on [JSON.com](http://www.json.com/2007/10/24/lossless-json-dates/ "Lossless JSON Dates").


API
===

Dove itself is only a server. A client is used to interact with a server (or multiple servers, if the client wants to support it). Due to the complex queries for tasks, such as according to tag, project, user, start date, due date, *range* of start or due dates, and probably more, Dove uses an RPC API. Specifically, [JSON-RPC](http://json-rpc.org/).

Dove instances will be able to be nodes as part of a "flock," an unplanned future feature where multiple Dove servers can communicate between each other and replicate tasks between nodes. The API for that is yet to be determined.

`searchTasks(selector)`
---------

`searchTasks(selector)` is a way to query for tasks by a generic selector. It takes one argument: a hash [dictionary] of options for selecting tasks. A task matching the selector are returned in an array. The selector is in this form:

    {
      option1: requirement1,
      option2: requirement2
      ...
    }

Generally, the selector options are identical to the task properties with a few exceptions. You can search for any task with the tag "home" with the following selector.

    {
        "tags": "home"
    }


  - `id` - an UUID or list of UUIDs. This option selects any task that matches one of these
  - `completed` - whether or not the tasks is completed
  - `tags` - an array of tags. This option selects all the tasks that are tagged with *each* of the items in `tags`.
  - `project` - an array of string UUIDs. This option selects all of the tasks whose project field is set to any of these ids.
  - `startDateRange` - an array with two elements, each of them a date. This option selects all tasks whose start date falls between those two dates. If the array consists of only one element, both elements are the same, or the first element is null, tasks that start *before* the given date are selected. If the second element is null, tasks that start *after* the given date are selected.
  - `dueDateRange` - similar to `startDateRange`.
  - `owner` - an array of string UUIDs. This option selects all the tasks belonging to any of the users listed in this array.

		// Example
		{
			"tags": ["home", "chores", "school"],
			"dueDateRange": ["2009-01-29T13:00:00-800", null],
			"owner": ["02b80516-a52f-4e94-bd07-05651ed00d98"]
		}

The above example will get all the tasks on the server which meet these requirements:

  - Tagged with all of home, chores, *and* school, or any subtags of those.
  - Due *after* January 29th, 2009 at 1 in the afternoon.
  - Belongs to the user with the id 02b80516-a52f-4e94-bd07-05651ed00d98.

When users are implemented, if a tag in `tags` has children in the tag dictionary belonging to the user specified in the `owner` option, tasks with those tags are selected as well. *CLARIFY*

Other Methods (explain further)
-------------------------------

  - `getTask(taskid)` is a quick way to get a single task by `taskid`. See [Tasks] for the tasks data definition.
  - `getTasks([taskid1, taskid2, ...])` is a quick way to get a group of tasks by `taskid`. See [Tasks] for the tasks data definition.
  - `createTask(task)` Takes a hash representing a task. See [Tasks] for required fields.
  - `updateTask(task)` Takes a hash representing a task. It must specify an id. Updates the task with any allowed attributes present in the hash.
  - `deleteTask(taskid)` Takes a string UUID representing a task. Removes the task from the system. Be careful. If a task has been completed, you should set its `completed` field to true.


TODO
====

This specification is a work in progress. It and any implementations based on it are likely to change frequently and drastically in this initial development stage. Here is a incomplete list of features yet to be fathomed.

  - Recurring/scheduled tasks
