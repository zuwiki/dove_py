Data
====

At the moment, Dove only uses one data model: the task. Pretty soon here, we'll also start talking about the user model.

Tasks contain this data:

  - identifier (a UUID)
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

`getTasks(selector)` is the main query method. It takes one argument: a hash [dictionary] of options for selecting tasks. Any tasks matching the selector are returned in an array. The selector is in this form:

    {
      option1: requirement1,
      option2: requirement2
      ...
    }

These selection options are available:

  - `id` -> a string UUID for the task. This option selects the task matching that id.
  - `completed` -> a boolean completion state for the task.
  - `tags` -> an array of tags. This option selects all the tasks that are tagged with *each* of the items in `tags`. [When users are implemented, if a tag in `tags` has children in the tag dictionary belonging to the user specified in the `owner` option, tasks with those tags are selected as well.]
  - `startDateRange` -> an array with two elements, each of them a date. This option selects all tasks whose start date falls between those two dates. If the array consists of only one element, both elements are the same, or the first element is null, tasks that start *before* the given date are selected. If the second element is null, tasks that start *after* the given date are selected.
  - `dueDateRange` -> similar to `startDateRange`.
  - `owner` -> a UUID for a user. This option selects all the tasks whose owner is the user represented by this UUID.

TODO
====

This specification is a work in progress. It and any implementations based on it are likely to change frequently and drastically in this initial development stage. Here is a incomplete list of features yet to be fathomed.

  - Recurring/scheduled tasks
  - Users, task ownership
  - Hierarchal tags defined in the user model. 