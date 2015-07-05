import os
import sys
#A-terms in c1&c2 not in b1&b2 , (c1 & c2) - (b1 & b2)
#G-terms in b1&b2 not in c1&c2 , (b1 & b2) - (c1 & c2)
#(A U G ) > threshold - synctactic cloaking

#if the parsed doc is available in b1,b2,c1,c2 then 

#calc function will be called everytime the button "Find URLS" under "CloakingDetection" tab of the GUI is pressed
def calc(arg):
        
    try:    
        threshold=int(arg)   
    except ValueError:
        print 'Threshold should be an integer.'
        return

    #will hold the final list of URLs which can be checked for cloaking 
    parsed=[]

    #as some of the URLS could not be parsed through browser's perspective because of the college restrictions on browsing of some websites, those webpages were ignored   
    accessDenied=''

   #the content parsed is compared with the parsed HTML content recieved by browser when a restricted page is tried to be accessed  
    with open('accessDenied.txt','r') as f:
        for line in f:
            accessDenied=line
            break
    
    #Iterate over all the parsed URLS returned by google for the top 10 query terms
    with open('url.txt','r') as f:
        
        for url in f: 
            url=url.strip()
            l=url.replace('/','_') #because a/b is used when b is in a folder, hence to remove ambiguity and to make os.path.isfile work correctly
            
            #ignore this URL if it could not be parsed for any of the 2 days for either browser perspective or crawler's perspective  
            if os.path.isfile('b1/' + l + '.txt') and os.path.isfile('b2/' + l + '.txt') and os.path.isfile('c1/' + l + '.txt') and os.path.isfile('c2/' + l + '.txt'):
                #if access not denied
                with open('b1/' + l + '.txt','r') as b1:
                    for line in b1:
                        if line is accessDenied:
                            continue
                        else:
                            parsed.append(url)
                        break
                    
            l= l + '%0A'
            
            if os.path.isfile('b1/' + l + '.txt') and os.path.isfile('b2/' + l + '.txt') and os.path.isfile('c1/' + l + '.txt') and os.path.isfile('c2/' + l + '.txt'):
                with open('b1/' + l + '.txt','r') as b1:
                    for line in b1:
                        if line is accessDenied:
                            continue
                        else:
                            parsed.append(url)
                        break         

    #Opening a file for writing results
    cp=open('CloakedPages.txt','w')
        
    for l in parsed:
        url=l
        l=l.replace('/','_') 
        d={}   #dictionary to find intersection of terms in expected linear time 
        b12=[] #list of terms which occur in both b1 and b2
        c12=[] #list of terms which occur in both c1 & c2
        b12d={} #dictionary of terms which occur in both b1 and b2
        c12d={} #dictionary of terms which occur in both c1 and c2
        A=[] #list of terms which occur on c1&c2 but not in b1&b2
        G=[] #list of terms which occur on b1&b2 but not in c1&c2
        
        if not os.path.isfile('b1/' + l + '.txt') or not os.path.isfile('b2/' + l + '.txt') or not os.path.isfile('c1/' + l + '.txt') or not os.path.isfile('c2/' + l + '.txt'):
        
            l= l + '%0A'
         
        #(c1 & c2)
        with open('c1/' +  l + '.txt') as f:
            for line in f:
                for word in line:
                    d[word]=1
                    
        with open('c2/' +  l + '.txt') as f:
            for line in f:
                for word in line:
                    if word in d.keys():    #term occured in c1 as well 
                        c12.append(word)
                        c12d[word]=1
                        
        d.clear() #to reuse it for b1&b2
        
        #(b1 & b2)                
        with open('b1/' +  l + '.txt') as f:
            for line in f:
                for word in line:
                    d[word]=1
                    
        with open('b2/' +  l + '.txt') as f:
            for line in f:
                for word in line:
                    if word in d.keys():
                        b12.append(word)    #term occured in c2 as well 
                        b12d[word]=1    
        
        #(c1 & c2) - (b1 & b2)                
        for word in c12:
            if word not in b12d.keys():        
                A.append(word)
        
        #(b1 & b2) - (c1 & c2)
        for word in b12:
            if word not in c12d.keys():        
                G.append(word)        
        
        #take union of A and G
        
        U={}
        
        c=0
        
        for word in A:
            if word not in U.keys():
                U[word]=1
                c=c+1  
                
        for word in G:
            if word not in U.keys():
                U[word]=1
                c=c+1
                   
        #compare with threshold 
        if c>threshold:
            cp.write(url.replace('%0A',''))
            cp.write('\n')
            
        print url + ' processed'    
    
 
    print str(len(parsed)) + " pages processed"
    
    cp.close()               
