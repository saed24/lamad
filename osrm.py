# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 22:08:08 2018

@author: Saeed
"""

try:
    from urllib.request import urlopen
except:
    from urllib2 import urlopen
    
import json


#r = urlopen("".join("))


def getRoutesFromOSRM(startPoint, endPoint, mode):
    
    url = 'http://router.project-osrm.org/route/v1/'+ mode+'/'+ startPoint['lat'] + ','+startPoint['lng'] +'\
    ;' +endPoint['lat'] + ','+ endPoint['lng']+ '?alternatives=2&geometries=geojson'

    rep = urlopen(''.join(url))
    parsed_json = json.loads(rep.read().decode('utf-8'))
    print(parsed_json)
    return parseCoordinates(parsed_json['routes'][0]['geometry']['coordinates'])
#response = urllib.request.urlopen(req).read()


def parseCoordinates(coord):
    
    route = []
    
    for x,y in coord:
        print(x)
        print(y)
        point = {}
        
        point['lat'] = float(x)
        point['lng'] = float(y)
        route.append(point)
    print(route)
    return route    
    


