import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://python-data.dr-chuck.net/comments_248356.xml'

#address = raw_input('Enter location: ')
#if len(address) < 1 : break

#url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
url  = serviceurl
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
print data
tree = ET.fromstring(data)


results = tree.findall('.//count')
#lat = results[0].find('geometry').find('location').find('lat').text
#lng = results[0].find('geometry').find('location').find('lng').text
#location = results[0].find('formatted_address').text

print sum(int(c.text) for c in results)
