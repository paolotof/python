# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
#from BeautifulSoup import *
from bs4 import *

def recursiveUrl(url,depth,count,position):

    if depth == count:
	print url
        return url
    else:
      html = urllib.urlopen(url).read()
      soup = BeautifulSoup(html)
      tags = soup('a')
      newlink = tags[position-1].get('href', None)
      return url, recursiveUrl(newlink,depth+1,count,position)

url = raw_input('Enter URL: ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

count = int(raw_input('Enter count : '))
position = int(raw_input('Enter position : '))

# Retrieve all of the anchor tags
tags = soup('a')
newlink = tags[position-1].get('href', None)
depth = 0
recursiveUrl(newlink,depth+1,count,position)
#for tag in tags:
   #print tag.get('href', None)


# html = urllib.urlopen(tags[position-1].get('href', None)).read()


      