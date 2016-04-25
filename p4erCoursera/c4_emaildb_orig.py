import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor() # this is to send the commands

# generate a new table everytime
cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: ') : continue
    pieces = line.split()
    email = pieces[1]
    # ? is a place older
    # (email, ) is a tuple
    # we are going to substitute ? with (emai, )
    # this is cacter substitution to avoid SQL injections
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email, ))
    try:
        count = cur.fetchone()[0]
        cur.execute('UPDATE Counts SET count=count+1 WHERE email = ?', (email, ))
    except:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES ( ?, 1 )''', ( email, ) )
    conn.commit() # write back to disk

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

# give me the top 10

for row in cur.execute(sqlstr) :
    # row 0 is the e-mail and row 1 is the count
    print str(row[0]), row[1]

cur.close()
