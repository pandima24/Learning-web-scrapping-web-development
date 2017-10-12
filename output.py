
import webPage


def writeToFile( state, title, url ):
    global f
    f = open(state+'-'+title+'.txt','w')
    titleArr = []
    titleArr.append( state )
    titleArr.append( title )
    recursiveParse(titleArr,url)
    f.close()


def recursiveParse(title,url):
    html = webPage.open(url)
    arr2 = title
    for li in html.find_all('li'):
        atag = li.find('a')
        if '?ID=' in atag['href']:
            if 'stateitem.php' not in atag['href']:
                arr2.append( atag.string )
                recursiveParse( arr2, 'http://www.workerscompensation.com/regulations/statedepartment.php'+atag['href'] )
            else:
                arr2.append( atag.string )
                finalURL = 'http://www.workerscompensation.com/regulations/' + atag['href']
                finalText(arr2, finalURL)
                # print atag['href']
                # for item in arr2:
                #     print item.encode('utf-8')
                arr2.pop()
                print '============================='
    print 'back --- true -------- next message ---'
    arr2.pop()


def finalText(title, url):
    global oneStateFullText
    global f
    html = webPage.open(url)
    summary = html.find("div", {"id": "summary"})
    paragrapph = summary  #.find_all('p')
    f.write('\n\n\n\n===================================================================\n')
    for item in title:
        f.write('--->' + item.encode('utf-8') )
    f.write('\n===================================================================\n')
    for p in paragrapph:
        if p.string is not None:
            # print p.string.encode('utf-8')
            f.write( p.string.encode('utf-8') )
        else:
            print p
            f.write( p.text.encode('utf-8') )
