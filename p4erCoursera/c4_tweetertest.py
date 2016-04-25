# import urllib
# from twurl import augment # this contains oauth - it is written by drchuck
#
# print '* Calling Twitter...'
# url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json',
#   {'screen_name': 'drchuck', 'count': '2'})
#
# print url
# connection = urllib.urlopen(url)
# data = connection.read() # this is the body
# print data # this is json data
# headers = connection.info().dict # this is a dictonary of the header
# print headers
#
#
# # more sophisticated application that does the same thing:
# # get friend list: and parse the list back
#
# import urllib
# import twurl
# import json
# TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
# while True:
#     print ''
#     acct = raw_input('Enter Twitter account:')
#     if (len(acct) < 1) : brek
#     url = twurl.augment(TWITTER_URL,
#         {'screen_name': acct, 'count': '5'}) # get 5 friends from this account
#     print 'Retrieving ', url
#     connection = urllib.urlopen(url)
#     data = connection.read()
#     headers = connection.info().dict
#     print 'Remaining ', headers['x-rate-limit-remaining']
#     js = json.loads(data)
#     print json.dumps(js, indent = 4) # debugging print command
#     for u in js['users'] :
#         print u['screen_name']
#         s = u['status']['text']
#         print '   ' , s[:50]
#

import json

data = '''{
    "users":[
        {
            "status":{
                "text":"@jazzychad I just bought one .__.",
            },
            "location":"San Francisco California",
            "screen_name":"leahculver",
            "name":"Leah Culver",

        }
    ]
}'''
info = json.loads(data)
#print 'Name: ' info[0]["name"]
print info["name"]
# print x['']
