# Report-Generator [WORK IN PROGRESS]
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
  "results": [
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
  ]
}
```

GET `/slides/<object_id>`: returns the HTML rendering of the slides using the [reveal-js](http://lab.hakim.se/reveal-js/#/fragments) library. If the `accept` header is set to `application/pdf`, then the endpoint will return a PDF version of the slides!


DELETE  `/slides/<object_id>`: deletes the slides with object_id equal to the supplied one


## DATABASE CONFIG
The database used is PostgreSQL, with SQLAlchemy as the ORM. Instructions for setting up the database:
Install PostgreSQL in your system:
```
$ sudo apt-get update
$ sudo apt-get install postgresql postgresql-contrib
```  
To make sure it is running:
```
$ sudo service postgresql start
```

Next, we will create a database and grant access to a new user:
```
$ sudo su - postgresql  #log into CLI
$ psql 
postgres=# CREATE USER new_user WITH PASSWORD 'password'; #Create a new user with it's password. DON'T FORGET TO END COMMAND WITH (;)
postgres=# CREATE DATABASE new_database;
postgres=# GRANT ALL PRIVILEGES ON DATABASE 'new_database' TO new_user;   #grant privileges to user 
postgres=# \q   #exit
```
Remember all this configurations, as you will need them to connect with it.
*If testing locally, always remember to start running the database*


