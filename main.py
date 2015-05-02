__author__ = 'Legendary Pegasus'


######this code just downloads a page from a url
#####resources are not downloaded so only online js,css and image references will work


import urllib2
import re
import locale

rate=60

#proxy = urllib2.ProxyHandler({'http': '192.168.64.98:809'})
#opener = urllib2.build_opener(proxy)
#urllib2.install_opener(opener)
page = urllib2.urlopen('http://money.cnn.com/2015/03/20/investing/fed-profit-balance-sheet/index.html')

page_content = page.read()








with open('page_content.html', 'w') as fid:
    fid.write(page_content)

