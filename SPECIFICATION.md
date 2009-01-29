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
  - tags (a list/array of strings each representing a tag)
  - [future] owner (a UUID representing the user responsible for a task)

All fields are optional except the identifier. However, you probably want a description so you know what the task is. Just saying.

Dates are encoded as text using the ISO 8601 format. More information is available on the [WWW Consortium website](http://www.w3.org/TR/NOTE-datetime "Date and Time Formats"), and an example is available on [JSON.com](http://www.json.com/2007/10/24/lossless-json-dates/ "Lossless JSON Dates").

API
===

Dove itself is only a server. A client is used to interact with a server (or multiple servers, if the client wants to support it). Due to the complex queries for tasks, such as according to tag, project, user, start date, due date, *range* of start or due dates, and probably more, Dove uses an RPC API. Specifically, [JSON-RPC](http://json-rpc.org/).

TODO
====

This specification is a work in progress. It and any implementations based on it are likely to change frequently and drastically in this initial development stage. Here is a incomplete list of features yet to be fathomed.

  - Recurring/scheduled tasks
  - Users, task ownership
