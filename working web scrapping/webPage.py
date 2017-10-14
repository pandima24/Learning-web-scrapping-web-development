import urllib2
from bs4 import BeautifulSoup
def open(url):
    page = urllib2.urlopen(url).read()
    soup = BeautifulSoup(page)
    soup.prettify()
    return soup

# for anchor in soup.findAll('a', href=True):
#     stateLink = anchor['href']
#     if '../' in stateLink:
#         print 'http://workerscompensation.com/' + stateLink.replace('../','')