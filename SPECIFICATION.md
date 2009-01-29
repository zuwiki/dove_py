Data
====

At the moment, Dove only uses one data model: the task.

Tasks contain this data:
  - identifier (a UUID)
  - description (a string)
  - note (a longer string, possibly RTF or HTML, and possibly stored as base64)
  - start date (a date and time with time defaulting to midnight)
  - due date (same)
  - tags (a list/array of strings each representing a tag)
  - owner (a UUID representing the user responsible for a task)

  All fields are optional except the identifier. However, you probably want a description so you know what the task is. Just saying.

API
===

Dove itself is only a server. A client is used to interact with a server (or multiple servers, if the client wants to support it). To ease development of Dove consumers, Dove uses a simple, lightweight API: REST. The transport format is JSON.