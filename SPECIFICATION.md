Data
====

At the moment, Dove only uses one data model: the task. Pretty soon here, we'll also start talking about the user model.

Tasks contain this data:

  - id (a UUID)
  - description (a string)
  - completed (boolean)
  - note (a longer string, possibly RTF or HTML, and possibly stored as base64)
  - start date (a date and time with time defaulting to midnight)
  - due date (same)
  - tags (a array of strings each representing a tag)
  - [future] owner (a UUID representing the user responsible for a task)
  - modification date (the date and time of the task's last change)

All fields are optional except the identifier. However, you probably want a description so you know what the task is. Just saying.

Dates are encoded as text using the ISO 8601 format. More information is available on the [WWW Consortium website](http://www.w3.org/TR/NOTE-datetime "Date and Time Formats"), and an example is available on [JSON.com](http://www.json.com/2007/10/24/lossless-json-dates/ "Lossless JSON Dates").

API
===

Dove itself is only a server. A client is used to interact with a server (or multiple servers, if the client wants to support it). Due to the complex queries for tasks, such as according to tag, project, user, start date, due date, *range* of start or due dates, and probably more, Dove uses an RPC API. Specifically, [JSON-RPC](http://json-rpc.org/).

`getTasks(selector)`
---------

`getTasks(selector)` is the primary query method. It takes one argument: a hash [dictionary] of options for selecting tasks. Any tasks matching the selector are returned in an array. The selector is in this form:

    {
      option1: requirement1,
      option2: requirement2
      ...
    }

All of the following selector options are optional:

  - `id` - an array of string UUIDs. This option selects each of the tasks whose ids are in the array.
  - `completed` - a boolean completion state for the task.
  - `tags` - an array of tags. This option selects all the tasks that are tagged with *each* of the items in `tags`. [When users are implemented, if a tag in `tags` has children in the tag dictionary belonging to the user specified in the `owner` option, tasks with those tags are selected as well.]
  - `project` > an array of string UUIDs. This option selects all of the tasks whose project field is set to any of these ids.
  - `startDateRange` - an array with two elements, each of them a date. This option selects all tasks whose start date falls between those two dates. If the array consists of only one element, both elements are the same, or the first element is null, tasks that start *before* the given date are selected. If the second element is null, tasks that start *after* the given date are selected.
  - `dueDateRange` - similar to `startDateRange`.
  - [future] `owner` - an array of string UUIDs. This option selects all the tasks belonging to any of the users listed in this array.

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

Other methods
-------------

 - `createTask(task)` -> Takes a hash representing a task. If you skipped the Data section, the only required attribute is an id, and that's created server-side, so you might just have an empty dictionary: `{}`
 - `updateTask(task)` -> Takes a hash representing a task. It must specify an id. Updates the task with any other attributes present in the hash.

TODO
====

This specification is a work in progress. It and any implementations based on it are likely to change frequently and drastically in this initial development stage. Here is a incomplete list of features yet to be fathomed.

  - Recurring/scheduled tasks
  - Users, task ownership
  - Hierarchal tags defined in the user model. 