# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 12:11:09 2018

@author: Saeed
"""
# http://cs.uef.fi/mopsi/routes/similarityApi/doc.html


try:
    from urllib.request import urlopen
except:
    from urllib2 import urlopen
    
import json
import handler

def getSimilarity(route1, route2):
   
    url = 'http://cs.uef.fi/mopsi/routes/similarityApi/?param={"measure":"C-SIM","threshold":25,"A":'+str(route1)+',"B":'+str(route2)+'}'
    
    url2 = url.replace(" ","")
    url2 = url2.replace("'",'"')
    print(url2)
    rep = urlopen(''.join(url2))
    parsed_json = json.loads(rep.read().decode('utf-8'))
    
    print(parsed_json)


