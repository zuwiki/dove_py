Data
====

Here are the data models, they are represented in the system as JSON objects.


Tasks
-----

  - `id` a unique task identifier
  - `summary` a short summary
  - `details` further task details, possibly a document stored as Base64
  - `completed` whether or not the task has been completed
  - `start` when the task begins
  - `due` when the task is due
  - `tags` a list of strings each representing a tag
  - `owners` a list or single user id
  - `lastmodified` datetime of the task's last change

Users
-----

  - `id` A unique hash represenation of the user
  - `email` The user's contact email address
  - `password` A salted hash of the users password
  - `fullname` The users's IRL full name
  - `tagtree` see [tagtree]


All fields are optional except the identifier. However, you probably want a description so you know what the task is. Just saying.

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

When users are implemented, if a tag in `tags` has children in the tag dictionary belonging to the user specified in the `owner` option, tasks with those tags are selected as well.] *CLARIFY*

The above example will get all the tasks on the server which meet these requirements:

  - Tagged with all of home, chores, *and* school, or any subtags of those.
  - Due *after* January 29th, 2009 at 1 in the afternoon.
  - Belongs to the user with the id 02b80516-a52f-4e94-bd07-05651ed00d98.

Other methods
-------------

  - `getTask(taskid)` is a quick way to get a single task by `taskid`. See [tasks] for the tasks data definition.
  - `getTasks([taskid1, taskid2, ...])` is a quick way to get a group of tasks by `taskid`. See [tasks] for the tasks data definition.
  - `createTask(task)` Takes a hash representing a task. If you skipped the Data section, the only required attribute is an id, and that's created server-side, so you might just have an empty dictionary: `{}`
  - `updateTask(task)` Takes a hash representing a task. It must specify an id. Updates the task with any other attributes present in the hash.
  - `deleteTask(taskid)` Takes a string UUID representing a task. Removes the task from the system. Be careful. If a task has been completed, you should set its `completed` field to true.



TODO
====

This specification is a work in progress. It and any implementations based on it are likely to change frequently and drastically in this initial development stage. Here is a incomplete list of features yet to be fathomed.

  - Recurring/scheduled tasks
  - Users, task ownership
  - Hierarchal tags defined in the user model. 


