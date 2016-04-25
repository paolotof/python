# beautiful soup

# beautifulSoup.py

# program which retrieves the webpage and parse it

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')

html = urllib.urlopen(url).read # this means read it all
soup = BeautifulSoup(html)

# retrieve a list of the anchor tags
# Each tag is like a dictionary of HTML attributes

tags = soup('a') # shows all the links in the page

for tag in tags:
  print tag.get('href', None) # none is the default
  
# this is the webscraper

http://www.dr.chuck.com/page1.html # possible link to use

# Q1
x = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')

# Q2
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')
while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print data
mysock.close()

# Q3  regular expressions to extract the URL from this line of HTML:

<p>Please click <a href="http://www.dr-chuck.com">here</a></p>

# href="(.+)"

I certify this submission as my own original work completed in accordance with the Coursera Honor Code