import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    address = raw_input('Enter location: ')
 #   address = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_42.xml'
    if len(address) < 1 : break

    #url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    #print 'Retrieving', url
    #uh = urllib.urlopen(url)
    uh = urllib.urlopen(address)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    # print data
    tree = ET.fromstring(data)


    results = tree.findall('.//count')
    #lat = results[0].find('geometry').find('location').find('lat').text
    #lng = results[0].find('geometry').find('location').find('lng').text
    #location = results[0].find('formatted_address').text

    #print 'lat',lat,'lng',lng
    #print location
    count = 0
    for elem in results:
      count = count + int(elem.text)
      
    print count