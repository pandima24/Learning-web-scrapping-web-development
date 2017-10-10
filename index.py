from bs4 import BeautifulSoup
import urllib2

page = urllib2.urlopen('http://workerscompensation.com/').read()
soup = BeautifulSoup(page)
soup.prettify()
for anchor in soup.findAll('a', href=True):
    stateLink = anchor['href']
    if '../' in stateLink:
        print stateLink

