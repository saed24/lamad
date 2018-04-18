# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 16:08:39 2018

@author: Raheel
"""

import handler as handler
import Distance as Distance

routes = handler.readRouteFromFile()
initial_long=routes[1]['lng']
initial_lat=routes[1]['lat']
total_distance=0

for i,obj in enumerate(routes[:-1]):
    #print(i['lat'],i['lng'])
   # j=i+1
    lat1=obj['lat']
    lon1=obj['lng']
    lat2=routes[i+1]['lat']
    lon2=routes[i+1]['lng']
    total_distance=total_distance+Distance.Distance(lat1,lon1,lat2,lon2)

print(total_distance)