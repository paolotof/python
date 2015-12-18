
# XML vs JSON

# write format - it is to go from python to the web

# serialize and deserialize: convert data in one program into a common format that can be stored and/or transmitted between systems in a programming language-independent manner. 

# eXtensible Markup Language (XML)

# it has advantage for documents. XML represents the choices of the document (e.g. fonts, etc)

# simple element <name>Chuck</name> - tag-text-tag

# complex element is a tag including another tag. 

# Start tag and end tag. Start tags have attributes <phone type="intl">+1 734 303 4456</phone>

# self closing tag - it opens and start into the same tag <email hide="yes"/>

# white spaces, indentation etc. usually do not matter, it is only for readability. You can always use pretty print in google and it will do it for you.

# in xml you make up the tags to describe things. It all has to do with the application that is going to use the data. So xml is very helpful, it is pretty and elegant. 

# XML is a text representation as a tree. There tends to be one text child and many child attributes. 

#/a/b : allows to follow the path to the text element into that child. And here you pull out what you need. 

## WHAT IS VALID XML?

# xml schema - xml validation. - xsd - w3 school xml schema

# you can next elements within elements using the same tags

# xsd constraints
# data is year, month, day, T hours, minutes, seconds Z (T = time; Z = time zone) ISO8601 for time

# maxOccurs="Unbounded" : it does not matter how many times it happen

## what do you do with XML in python?

# xml is built into python. 

import urllib 
import xml.etree.ElementTree as ET

# xml is into a string, but there is an xml parsing element built-in into python

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    print data
    tree = ET.fromstring(data) # this is parsing the xml string: DESERIALIZING


    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    #print 'Name: ' tree.find('name').text
    #print 'Attr: ' tree.find('email').get('hide')
    #stuff = ET.fromstring(input)
    #lst = stuff,findall('users/user') # this is a path where to search. Output is stored in the list
    # then you can loop through the items in the list. The items in the list are also xml nodes. so
    # there you can find other attributes.  
    print 'lat',lat,'lng',lng
    print location







