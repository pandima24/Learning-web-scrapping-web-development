
def getLinks(html):
    links = []
    for atag in html.findAll('a', href=True):
        href = atag['href']
        if 'statedepartment.php?' in href:
            links.append( 'http://www.workerscompensation.com/regulations/' + href )
    return links