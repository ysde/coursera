import urllib
from bs4 import BeautifulSoup

def retrive_link(url, nth, repeat, limit):
    count = 1
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    for tag in tags:
        #print repeat, limit
        #print(tag)
        #print count, nth
        if (count == nth):
            if (repeat == limit):
                return tag.contents[0]
            link = tag['href']
            print("Retriving:" + link)
            return retrive_link(link, nth, repeat + 1, limit)
            break
        count += 1

#url = raw_input('Enter: ')
url = "http://python-data.dr-chuck.net/known_by_Duncan.html"

print retrive_link(url, 18, 1, 7)
