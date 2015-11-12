# connection to a server

import socket # library to access the internet

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))

# HTTP is a set of rules on who says something to somebody else. Who is going first?
# Uniform resource locator: URL
# you get three informations in there:
# 1) the protocol - http://
# 2) the host - www.dr-chuck.com
# 3) the document - /page1.html
# URL interprets all these three languages into one.

# request-response cycle: at the moment you click it makes a request and you then get a response.

mysock.send('GET  http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

while True:
  data = mysock.recv(512)
  if (len(data) < 1):
    break
  print data
  
mysock.close()

# blank line is the separation between head and body of the html file

# there is another library which makes it simpler

import urllib
fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')

for line in fhand:
  print line.strip()

# URL libs report the body and skips the rest. You can get it, but mostly isn't very helpful, or people don't want to use it.

counts = dict()
for line in fhand:
  words = line.split()
  for word in words:
    counts[word] = counts.get(word,0) + 1
    
print counts
