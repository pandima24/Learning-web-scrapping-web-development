from bs4 import BeautifulSoup
import urllib2

# page = urllib2.urlopen('http://workerscompensation.com/').read()
# soup = BeautifulSoup(page)
# soup.prettify()
# for anchor in soup.findAll('a', href=True):
#     stateLink = anchor['href']
#     if '../' in stateLink:
#         print 'http://workerscompensation.com/' + stateLink.replace('../','')

states = [
    'alabama',
    'alaska',
    'arizona',
    'arkansas',
    'california',
    'colorado',
    'connecticut',
    'delaware',
    'florida',
    'georgia',
    'hawaii',
    'idaho',
    'illinois',
    'indiana',
    'iowa',
    'kansas',
    'kentucky',
    'louisiana',
    'maine',
    'maryland',
    'massachusetts',
    'michigan',
    'minnesota',
    'mississippi',
    'missouri',
    'montana',
    'nebraska',
    'nevada',
    'new_hampshire',
    'new_jersey',
    'new_mexico',
    'new_york',
    'north_carolina',
    'north_dakota',
    'ohio',
    'oklahoma',
    'oregon',
    'pennsylvania',
    'rhode_island',

]
