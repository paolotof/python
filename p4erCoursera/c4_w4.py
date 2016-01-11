Many to Many relationships

\Lecture 1 MANY TO MANY

https://en.wikipedia.org/wiki/One-to-many_(data_model)

https://en.wikipedia.org/wiki/Many-to-many_(data_model)

# In this case you put a table in the middle that is modeling the connection among other tables. For example, this table has two foreign keys and no primary keys.

# START WITH A FRESH DATABASE

CREATE TABLE User(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT,
    email TEXT
)

CREATE TABLE Course(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT
)

# there is no primary key, but we make it a composite key
CREATE TABLE Member(
    user_id INTEGER,
    course_id INTEGER
        role INTEGER,
    PRIMARY KEY (user_id, course_id) # COMPOSITE KEY: it is forced to be unique because of the requirements by user_id and course_id
)

# insert some data: users and courses
INSERT INTO User (name, email) VALUES ('Jane', 'jane@tsugi.org');
INSERT INTO User (name, email) VALUES ('Ed', 'ed@tsugi.org');
INSERT INTO User (name, email) VALUES ('Sue', 'sue@tsugi.org');

INSERT INTO Course (title) VALUES ('Python');
INSERT INTO Course (title) VALUES ('SQL');
INSERT INTO Course (title) VALUES ('PHP');

# insert memberships
INSERT INTO Member (user_id, course_id, role) VALUES (1, 1, 1);
INSERT INTO Member (user_id, course_id, role) VALUES (2, 1, 0);
INSERT INTO Member (user_id, course_id, role) VALUES (3, 1, 0);

INSERT INTO Member (user_id, course_id, role) VALUES (1, 2, 0);
INSERT INTO Member (user_id, course_id, role) VALUES (2, 2, 1);

INSERT INTO Member (user_id, course_id, role) VALUES (2, 3, 1);
INSERT INTO Member (user_id, course_id, role) VALUES (3, 3, 0);


# getting data out
SELECT User.name, Member.role, Course.title
FROM User JOIN Member JOIN Course
ON Member.user_id = User.id AND Member.course_id = Course.id
ORDERED BY Course.title, Member.role DESC, User.name

# data are organized in this way because of speed. It makes data management very very efficient.
