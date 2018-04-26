# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 13:20:00 2018

@author: Raheel
"""

import json
import urllib.request as urs
import directionsdecode as dd

def googledirections(lat1,lng1,lat2,lng2):
    
    url2='https://maps.googleapis.com/maps/api/directions/json?&alternatives=true&mode=walking&origin='+str(lat1)+ \
    ','+str(lng1)+'&destination='+str(lat2)+','+str(lng2)+  \
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
    return(route_all)