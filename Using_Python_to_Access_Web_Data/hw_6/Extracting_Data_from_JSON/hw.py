import json
import urllib

url = 'http://python-data.dr-chuck.net/comments_248360.json'
input = urllib.urlopen(url).read()
info = json.loads(input)
print 'input:', info

print sum([item['count'] for item in info['comments']])


