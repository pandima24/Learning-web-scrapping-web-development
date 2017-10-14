from bs4 import BeautifulSoup
import urllib2


import states
import webPage
import parseStateHomePhp
import output

for state in states.name:
    url = 'http://www.workerscompensation.com/regulations/statehome.php?state=' + state
    #print url
    html = webPage.open(url)
    stateHomeLinks = parseStateHomePhp.getLinks(html)
    #print stateHomeLinks
    i = 0
    for stateDepartmentLink in stateHomeLinks:
        # if i == :
        #     i = i+1
        output.writeToFile( state, stateDepartmentLink['title'], stateDepartmentLink['url'] )
    print '---------------------------------'

