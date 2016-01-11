MULTI-TABLE RELATIONAL SQL

Data models and relational sqlite

\Lecture 1 Designing a Data Model

# we make a Schema and contract, and than there are a lot of tables and some columns and some connections.
# Connections are what make this powerful.

# RULES;
# 1 - Don't put the smae string data in twice - use a relationship instead!
# 2 - model the real world

# make a track making thing:
# problem: data replication in columns (e.g. band name, name of the album name of a genre). The replication is a problem because it takes a lot of space.
# You want to write an efficient interface that manages the data efficiently but still makes the user see what he wants to see.
# Where do you start from:
# it does not make a lot of difference but think about the thing is the most essential for the application: in this case is 'track managing'.
# you need to look at the data and try to figure out a structure.
# a track table with field title. What is connected to that? Album? What does album belongs to? A group/band. What does genre connect to?
# what changes when you change something in your database? Genre belongs to track.
# What is in the datamodel determines what the interface can do.

\Lecture 2 IMPLEMENTING A DATA MODEL IN TABLES

# Primary key: a unique number referring to a row. They are the end-points we are pointing to.
# Foreign key: colum that we add which represents the starting point of the table.
# logical key: key one might use to look up this thing from the outside world. We might use in a ordered clause..
# this is the ruby on rails naming convention.
# the tendency is to work outside-in.
CREATE TABLE Genre(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT
)
# example with foreign key
CREATE TABLE Album(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER, # this is the foreign key
    title TEXT
)
# example with 2 foreign keys.
CREATE TABLE Track(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT,
    album_id INTEGER, # this is the foreign key
    genre_id INTEGER, # this is the foreign key
    len INTEGER, rating INTEGER, count INTEGER
)

\Lecture 3 INSERTING DATA

insert into Artist (name) values ('AC/DC');
insert into Artist (name) values ('Led Zeppelin')

# you do not need to assign an id, it does it automatically
insert into Genre (name) values ('metal');
insert into Genre (name) values ('rock')

# album requires a foreign id because it points also to Artist
# you do not want to do this by hand, so you need the number which you can find that out
insert into Album (title, artist_id) values ('Who made who', 2);
insert into Album (title, artist_id) values ('IV', 1);

# Adding two foreign keys, there is replication here, but replication is not a problem as long as it uses numbers:
insert into Track (title, rating, len count, artist_id, genre_id) values ('Black Dog', 5, 297, 0, 2, 1);
insert into Track (title, rating, len count, artist_id, genre_id) values ('Stairway', 5, 482, 0, 2, 1);
insert into Track (title, rating, len count, artist_id, genre_id) values ('Who made who', 5, 207, 0, 1, 2);
insert into Track (title, rating, len count, artist_id, genre_id) values ('Who made who', 5, 207, 0, 1, 2)

# Databases try to reduce the amount of information that has to be scanned to reach a response.

\Lecture 4 RECONSTRUCTING DATA WITH JOIN

#Relational power: by removing the replicated data and replacing it with references to a single copy of each bit of data we build a 'web' of information that the relational database cn go through very quickly - even for  large amounts of dataself.
#Often when you want some data it comes from a number of table linked by foreign keys.

#The JOIN operation allows to connect all these table together. It is part of the select operation and it allows linking accross several tables.
#The call to JOIN must specify how to use the keys that make the connection between the table. This is done through an ON clause.

select Album.title, Artist.name from Album join Artist on Album.artist_id = Artist_id

# from specifies from Where
# on specifies what links the two tables, it's like an arrow pointing to the right rows.

# we can see how the connection is made by adding Album.artist_id, Artist.id as in:
select Album.title, Album.artist_id, Artist.id, Artist.name from Album join Artist on Album.artist_id = Artist_id

# they do not need to be shown, but they are the source of the connection

# what happens if you remove the 'on clause': then it returns all combinations.
# JOIN is building accross all table all possible combinations (paol8: so it is a sort of data replication?)
# with the ON clause you pick the combinations.

# it can get complex, but it has a pattern and it's therefore straigtforward:
SELECT Track.title, Artist.name, Album.title, Genre.name FROM Track JOIN Genre JOIN Album JOIN Artist ON Track.genre_id = Genre.id AND Track.album.id = Abum.id AND Album.artist_id = Artist.id

# the replication is only on the output, not in the data itself.

\Lecture 5 MULTI-TABLE DEMO
# Connecting xml and databases

#File Export (playlist) from itunes then you get an xml file.
plist = property list. Then there are dictionaries.
