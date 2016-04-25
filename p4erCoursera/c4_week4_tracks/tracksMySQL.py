import xml.etree.ElementTree as ET
#import sqlite3
#python /home/paolot/gitStuff/python/p4erCoursera/week4_tracks/tracksMySQL.py
import MySQLdb

#conn = sqlite3.connect('trackdb.sqlite')
conn = MySQLdb.connect (host = "localhost",
                        user = "root",
                        passwd = "Ciao8&LL0",
                        db = "company")
cur = conn.cursor()

# Make some fresh tables using executescript()
#cur.executescript("
cur.execute("""DROP TABLE IF EXISTS Artist""")
cur.execute("""DROP TABLE IF EXISTS Album""")
cur.execute("""DROP TABLE IF EXISTS Track""")
cur.execute("""DROP TABLE IF EXISTS Genre""")

cur.execute("""CREATE TABLE Artist 
  (
    id int NOT NULL AUTO_INCREMENT UNIQUE,
    name varchar(255) UNIQUE, 
    PRIMARY KEY (id) 
)""")

cur.execute("""CREATE TABLE Album (
    id int NOT NULL AUTO_INCREMENT UNIQUE,
    artist_id  int,
    title  varchar(255) UNIQUE
    PRIMARY KEY (id) 
)""")

cur.execute("""CREATE TABLE Track (
    id int NOT NULL AUTO_INCREMENT UNIQUE,
    title varchar(255)  UNIQUE,
    album_id  int,
    genre_id  int,
    len int, rating int, count int
    PRIMARY KEY (id) 
)""")

cur.execute("""CREATE TABLE Genre (
    id int NOT NULL AUTO_INCREMENT UNIQUE,
    name  varchar(255) UNIQUE
    PRIMARY KEY (id) 
)""")


fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'Library.xml'

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print 'Dict count:', len(all)
for entry in all:
    if ( lookup(entry, 'Track ID') is None ) : continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    genre = lookup(entry, 'Genre')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    if name is None or artist is None or album is None or genre is None:
        continue

    print name, artist, album, count, rating, length, genre

    cur.execute("""INSERT OR IGNORE INTO Artist (name)
        VALUES ( ? )""", ( artist, ) )
    cur.execute("""SELECT id FROM Artist WHERE name = ? """, (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute("""INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES ( ?, ? )""", ( album, artist_id ) )
    cur.execute("""SELECT id FROM Album WHERE title = ? """, (album, ))
    album_id = cur.fetchone()[0]

    # cur.execute("""INSERT OR REPLACE INTO Genre (genre)
    cur.execute("""INSERT OR IGNORE INTO Genre (name)
        VALUES ( ? )""", ( genre, ) )
        # what do the lines below do?
    cur.execute("""SELECT id FROM Genre WHERE name = ? """, (genre, ))
    genre_id = cur.fetchone()[0]
    # print genre_id

    # why is it replace here instead of ignore?
    cur.execute("""INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count)
        VALUES ( ?, ?, ?, ?, ?, ?)""",
        ( name, album_id, genre_id, length, rating, count ) )
    # also other commands are missing

    conn.commit()
