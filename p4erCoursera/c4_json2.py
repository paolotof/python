import urllib
import json

# input = '''
# [
#   { "id" : "001",
#     "x" : "2",
#     "name" : "Chuck"
#   } ,
#   { "id" : "009",
#     "x" : "7",
#     "name" : "Chuck"
#   }
# ]'''

while True:
    address = raw_input('Enter location: ')
#    address = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_42.json'
    if len(address) < 1 : break

    print 'Retrieving', address

    connection = urllib.urlopen(address)
    data = connection.read()
    print 'Retrieved',len(data),'characters'
    # print data

    info = json.loads(data)

    print 'User count:', len(info['comments'])
    sum = 0
    for item in info['comments']:
        sum = sum + int(item['count'])
        # print 'Name', item['name']
        # print 'Id', item['count']

    print 'Sum: ', sum
