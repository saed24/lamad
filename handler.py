# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 09:49:34 2018

@author: Saeed
"""
from math import sin, cos, sqrt, atan2, radians
import os
import GridPy as grid
import frequency as f

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

def OuterRoute(routes, A, B):
    
    #print('outer route')
    A=DividingRoute(routes,1,A)
    B=DividingRoute(routes,B,100)
    mergelist= A+B
    #print(A[-1])
    #print(B[0])
    return mergelist, A[-1], B[0]

def Probability(route,route2,y):

    grid_1=grid.pointsToWGSCells(route,1000)
    grid_2=grid.pointsToWGSCells(route2,1000)
    centroids=[]
    
    print("1")
    for x in range(0, len(grid_1)):
        centroid={}
        centroid["_id"] = x
        centroid["lat"] = round((float(int(grid_1[x]['northing'])/1000)),8)
        centroid["lng"] = round((float(int(grid_1[x]['easting'])/1000)),8)
        centroids.append(centroid)
    
    dict1=f.returnToDict(grid_1)
    dict2=f.returnToDict(grid_2)

    counter1=0
    counter2=0

    for k,v in y.items():
        if k in dict1:
            counter1=counter1+v
            # print(counter1)
            if k in dict2:
                counter2=counter2+v

    base=counter1+counter2
    if base==0:
        base=1
    
    #print('probability handler')
    
    counter1=round((counter1/base)*100)
    counter2=round((counter2/base)*100)
    
    if counter1>counter2:
        return counter1 , route , route2 , centroids
    if counter2>counter1:
        return counter2 , route2 , route , centroids
    


def Probability2(route : list ,y):
    print(len(route))
    print(type(route))
    grid_1=[]
    dict_1=[]

    for x in range(0, len(route)):
        
        print(route[x])
        grid_1.append(grid.pointsToWGSCells(route[x],1000))
        print(grid_1[x])
        dict_1.append(f.returnToDict(grid_1[x]))
    
    counter=[0]*len(dict_1)

    for k,v in y.items():
        for z in range(0, len(dict_1)):
            if k in dict_1[z]:
                counter[z]=counter[z]+v
    
    
    centroids=[]
    index_of_max=counter.index(max(counter))
    base=sum(counter)
    if base==0:
        base=1
    
    for x in range(0, len(counter)):
        counter[x]=round((counter[x]/base)*100)
    
    for x in range(0, len(grid_1[index_of_max])):
        centroid={}
        centroid["_id"] = x
        centroid["lat"] = round((float(int(grid_1[index_of_max][x]['northing'])/1000)),8)
        centroid["lng"] = round((float(int(grid_1[index_of_max][x]['easting'])/1000)),8)
        centroids.append(centroid)
    
        return counter[index_of_max] , route[index_of_max], route[~index_of_max] , centroids






