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


def getRoutesFromOSRM(startPoint, endPoint, alternatives, mode):
    
    url = 'http://router.project-osrm.org/route/v1/'+ mode+'/'+ startPoint['lng'] + ','+startPoint['lat'] +'\
    ;' +endPoint['lng'] + ','+ endPoint['lat']+ '?alternatives='+alternatives+'&geometries=geojson'

    rep = urlopen(''.join(url))
    parsed_json = json.loads(rep.read().decode('utf-8'))
    print(parsed_json)
    return parsed_json['routes'][0]['geometry']['coordinates']
#response = urllib.request.urlopen(req).read()

startPoint = {'lng': '62', 'lat': '28'}
endPoint = {'lng': '62', 'lat': '27.5'}

getRoutesFromOSRM(startPoint, endPoint, '3', 'walking')