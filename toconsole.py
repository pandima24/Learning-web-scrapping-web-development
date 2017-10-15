# import libraries
# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
quote_page = 'http://www.google.com'
page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
print soup.encode('utf-8')