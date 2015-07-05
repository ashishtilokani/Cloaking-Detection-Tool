# import libraries
import requests
from bs4 import BeautifulSoup as BS
import time
import re
import sys
import codecs

# settings
keywords = []
timeout = 30000
results = 0
# initialize session
s = requests.session()

print 'Generating URLs.txt'

with open('TopQueries.txt','r') as f:
    for line in f:
           keywords.append(line)  

f = open('url.txt','w')

# set headers
s.headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

t = time.time()
for keyword in keywords:
    get_results = s.get('https://www.google.com/search?num=100&q='+str(keyword)+'&safe=off', timeout = timeout)
    soup = BS(get_results.content)
    # get the text results, exclude images.
    for srg in soup.findAll(attrs={'class' : 'srg'}):
        for li in srg.findAll('li', attrs={'class' : 'g'}):
                #results.append(li.h3.text)
                sLink = li.find('a')
                
                UTF8Writer = codecs.getwriter('utf8')
                sys.stdout = UTF8Writer(sys.stdout)   
                    
                f.write(sLink['href'] )
                
                f.write('\n')
    
    get_results = s.get('https://www.google.com/search?num=100&q='+str(keyword)+'&safe=off&start=100', timeout = timeout)
    soup = BS(get_results.content)
    # get the text results, exclude images.
    for srg in soup.findAll(attrs={'class' : 'srg'}):
        for li in srg.findAll('li', attrs={'class' : 'g'}):
                #results.append(li.h3.text)
                sLink = li.find('a')
                
                UTF8Writer = codecs.getwriter('utf8')
                sys.stdout = UTF8Writer(sys.stdout)   
                    
                f.write(sLink['href'] )
                
                f.write('\n')
                
                
f.close()    
                
print 'Elapsed time:',time.time() - t
