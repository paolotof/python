\Lecture 1 Data bases

Install database browser:
DB browser for SQLite (SQlite browser)

Relational Databases

Schema and rules

Structured Query Language is the language to issue commands to the database

create table
retrieve data
insert data
update data
delete data

API : application program interfaceself.

SQL: depends on the data being pretty. Python instead handles messy data very nicely.

\Lecture 2 Using Databases


Relational database - Structured Query Language

Database, relation (or table), tuple (row), and attributes (column)

You model everything as a connection.

Schema.

Application Programming Interface

Service or architecture talk to our API in SQL.

Python cleans up the data and SQL stores it up.

\Lecture 02 Using Databases

Large project (website)
There are two main functions in such a project: 1 - Application developer (create applications software) and 2 - database administrator.

Small projects

SQLite - it's an embedded database. It's easy, simple and small.

Database model: the schema tells to the database what to do with the data.

\Lecture 03 Single Table CRUD

Save a new database.

Then go to the tab Execute SQL and insert the command to create a table

CREATE TABLE Users(
    name VARCHAR(128),
    email VARCHAR(128)
)

The we put some data into the table clicking on New Record.

INSERT INTO Users (name, email) VALUES ('paolo', 'fuck@you')

DELETE FROM Users WHERE email='ted@umich.edu'

UPDATE Users SET name='Charles' WHERE email='csev@umich.edu' # this is to change values

# selects everything
SELECT * FROM Users
# selects teh users with that e-mail address
SELECT * FROM Users WHERE email='csev@umich.edu'
# select and sort
SELECT * FROM Users ORDERED BY email
SELECT * FROM Users ORDERED BY name
# count number of users
SELECT COUNT(*) FROM Users
