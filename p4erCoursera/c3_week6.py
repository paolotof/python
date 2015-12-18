#dictionary are objects in json and lists are arrays in json.

# in json there are no attributes as in XML

# we need to deserialize
import json

dat = '''{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+ 1 23456 67"
  
  },
  "email" : 
  {
    "hide" : "yes";
  }
}'''

info = json.loads(data) # deserialize command
# info is a dictionary 

print 'Name:', info["name"]
print 'Hide:', info["email"]["hide"]

# arrays are made with square braces

input = '''[
  { "id" : "001"
    "x" : "2"
    "name" : "Chuck"
  },
  { "id" : "009"
    "x" : "7"
    "name" : "Chuck"
  }
]'''

info json.loads(input)
print 'User count:', len(info)
for item in info:
  print 'Name', item['name']
  print 'Id', item['id']
  print 'Atrtibute', item['x']
  
# REST instead of SOAP

# google geocoding API


import urllib
form twurl import augment

print '* Calling Twitter...'

url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json',
  {'screen_name': 'drchuck', 'count': '2'})

print url

connection = urllib.openurl(url)
data = connection.read()
print data
header = connection.info().dict
print headers