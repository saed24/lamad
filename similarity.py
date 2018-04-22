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
   
    url = 'http://cs.uef.fi/mopsi/routes/similarityApi?param={"measure":"C-SIM","threshold":25,"A":'+str(route1)+',"B":'+str(route2)+'}'
    
    url2 = url.replace(" ","")
    print(url2)
    rep = urlopen(''.join(url2))
    parsed_json = json.loads(rep.read().decode('utf-8'))
    
    print(parsed_json)

route1 = handler.readRouteFromFileWOTimeAndAlt('1372602289525')
route2 = handler.readRouteFromFileWOTimeAndAlt('1372604194383')

r1 = []
r2 = []
for x in range(0,3):
    point = {}
    point = route1[x]
    r1.append(point)
    point = {}
    point = route2[x]
    r2.append(point)


print(r2)

getSimilarity(r1, r2)