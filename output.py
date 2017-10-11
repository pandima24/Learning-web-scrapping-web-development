
import webPage

def writeToFile( state, title, url ):
    titleArr = []
    titleArr.append( state )
    titleArr.append( title )
    recursiveParse(titleArr,url)

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
                print atag['href']
                print arr2
    #print returnArr2