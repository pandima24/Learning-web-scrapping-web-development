

def getLinks(html):
    links = []
    for atag in html.findAll('a', href=True):
        href = atag['href']
        if 'statedepartment.php?' in href:
            obj = {}
            obj['title'] = atag.string
            obj['url'] = 'http://www.workerscompensation.com/regulations/' + href
            links.append( obj )
    return links
