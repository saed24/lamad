# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 09:49:34 2018

@author: Saeed
"""
from math import sin, cos, sqrt, atan2, radians
import os

R = 6373.0 # approximate radius of earth in km

def readRouteFromFile(filepath):
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
    #print(routes)            
    return routes

def readRouteFromFileWOTimeAndAlt(filepath):
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
                
                routes.append(points)
    #print(routes)            
    return routes

def readRoutesFromFolder():
    path = './MopsiRoutes2014/routes/13/'
    routes2 = []  
    counter = 0  
    for filename in os.listdir(path):
        counter = counter + 1
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

def Distance(lat1,lon1,lat2,lon2): # Calculates distance between two points
    
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)
    
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance


def PathDistance(routes): # Calculates Total distance of the path
    total_distance=0

    for i,obj in enumerate(routes[:-1]):
        lat1=obj['lat']
        lon1=obj['lng']
        lat2=routes[i+1]['lat']
        lon2=routes[i+1]['lng']
        total_distance=total_distance+Distance(lat1,lon1,lat2,lon2)
    return total_distance


def DividingRoute(routes, A, B):
    A=int (len(routes)*(A/100))
    B=int (len(routes)*(B/100))
    return routes[A:B]


