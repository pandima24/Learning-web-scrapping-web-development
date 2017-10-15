# import libraries
# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
url = 'http://www.google.com'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
for element in soup.findAll('div'):
 print element
for aelement in soup.findAll('a'):
    print aelement