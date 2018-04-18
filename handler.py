# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 09:49:34 2018

@author: Saeed
"""

import sys
import json

def readRouteFromFile():
    filepath = '1365683861651'
    routes = []
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            points = {}
            line = fp.readline()
            temp = line.split(' ')
                
            if len(temp) == 4:
                points['lat'] = float(temp[0])
                points['lng'] = float(temp[1])
                points['time'] = temp[2]
                points['alt'] = temp[3]
                print(points);
                routes.append(points)
                
    return routes