import urllib
from bs4 import BeautifulSoup

url = "http://python-data.dr-chuck.net/comments_248359.html"

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('span')

print sum([int(tag.contents[0]) for tag in tags])

#for tag in tags:
#    print(int(tag.contents[0]))
