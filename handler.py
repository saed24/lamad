# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 09:49:34 2018

@author: Saeed
"""

import os


def readRouteFromFile():
    filepath = '1216652978620'
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
                
                routes.append(points)
    print(routes)            
    return routes


def readRoutesFromFolder():
    path = 'C:/Users/Raheel/PathPrediction/MopsiRoutes2014/routes/1/'
    counter=0
    routes2 = []    
    for filename in os.listdir(path):
        counter=counter+1
        with open(path+filename,"r") as fp:
            line = fp.readline()
            while line:
                points = {}
                line = fp.readline()
                temp = line.split(' ')
                    
                if len(temp) == 4:
                    points['routeid'] = counter
                    points['lat'] = float(temp[0])
                    points['lng'] = float(temp[1])
                    points['time'] = temp[2]
                    points['alt'] = temp[3]
                    #print(points);
                    routes2.append(points)
    return routes2