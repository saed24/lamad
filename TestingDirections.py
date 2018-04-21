# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 14:42:07 2018

@author: Raheel
"""

import json
import urllib.request as urs
import directionsdecode as dd
 
url2='https://maps.googleapis.com/maps/api/directions/json?&alternatives=true&mode=walking&origin='+str(62.6010)+ \
','+str(29.7636)+'&destination='+str(60.1699)+','+str(24.9384)+  \
'&key=AIzaSyBZKdJjHvjlTDNjM4LHaNgKmkQmSb0GmtA'

ur = urs.urlopen(url2)
result = json.load(ur)
#print(result)

encoded_path = {}
#print(len(result['routes']))
for x in range(0,len(result['routes'])):
    encoded_path[x]=(result['routes'][x]['overview_polyline']['points'])
    #print(x)

decoded_path = {}
print(len(encoded_path))
for x in range(0,len(encoded_path)):
   decoded_path[x]=dd.decode(encoded_path[x])

route_all=[]
for x in range(0,len(decoded_path)):
    route = []
    for i in range(0,len(decoded_path[x])):
        point = {}        
        point['lat'] = decoded_path[x][i][1]
        point['lng'] = decoded_path[x][i][0]
        route.append(point)
        #print(route)
    route_all.append(route)