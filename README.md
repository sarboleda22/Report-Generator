# Report-Generator
A flask micro-service to generate PDF reports based on markdown input


# API Overview

## /slides

POST `/slides/`: creates a new set of slides

  - name<TextField>: a name of the slides
  - object_id<UUID>: a unique identifier for the slides. Need to be automatically assigned by the server when a new POST request is made
  - content<TextField>: markdown body of the slides
  
GET  `/slides/`: returns a list of all the slides in the following format:

```
{
  "count": 10,
  "results": {
    {
      "name": "name",
      "object_id": "uuid"
    },
        {
      "name": "name",
      "object_id": "uuid"
    },
    {
      "name": "name",
      "object_id": "uuid"
    },
    {
      "name": "name",
      "object_id": "uuid"
    },
    {
      "name": "name",
      "object_id": "uuid"
    },
    {
      "name": "name",
      "object_id": "uuid"
    },
    {
      "name": "name",
      "object_id": "uuid"
    },
    {
      "name": "name",
      "object_id": "uuid"
    },
    {
      "name": "name",
      "object_id": "uuid"
    },
    {
      "name": "name",
      "object_id": "uuid"
    }
  }
}
```

GET `/slides/<object_id>`: returns the HTML rendering of the slides using the [reveal-js](http://lab.hakim.se/reveal-js/#/fragments) library. If the `accept` header is set to `application/pdf`, then the endpoint will return a PDF version of the slides!


  
