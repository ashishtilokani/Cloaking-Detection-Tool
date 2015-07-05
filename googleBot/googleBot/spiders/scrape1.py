from scrapy.selector import HtmlXPathSelector
from scrapy.spider import Spider
import html2text
import re
import os.path

class scrape(Spider):
    name = "googleBot1"

    start_urls = []
    
    with open('/home/ashish/Desktop/CloakingDetectionTool/url.txt','r') as f:
        for line in f:
            l=line.replace("/", "_")
            try: 
                f=open('/home/ashish/Desktop/CloakingDetectionTool/c1/'+ l + '.txt','r')
                f.close()
            except:
                start_urls.append(line)
                           
    def parse(self, response):
        regex = re.compile('[^A-Za-z0-9_]')
        #First parameter is the replacement, second parameter is your input string
        d={}
        l=(response.url).replace("/", "_")
        f=open('/home/ashish/Desktop/CloakingDetectionTool/c1/'+ l + '.txt','w')
        terms=[]
        terms = (response.body).split()
        c=0
        for word in terms:
            word=regex.sub('', word) 
            if word not in d:    
                d[word]=1
                f.write(word)
                f.write(' ') 
                c=1
                
        if c==0:     #empty    
            f.write(' ')
        f.write('\n')
        f.close()
