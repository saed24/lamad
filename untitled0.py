# -*- coding: utf-8 -*-
"""
Created on Fri May 11 21:32:20 2018

@author: Raheel
"""


        
import frequency as f
import handler as handler
import googledirections as gd
import json

y=f.addPointsToDict('1')

route=handler.readRouteFromFile('1216481888112')
A = 20
B = 90
#print(route)
outroute, first, second =handler.OuterRoute(route,A,B)

newlist=[]
newlist.append( str(first['lat']) + "," + str(first['lng']))
newlist.append(str(second['lat']) + "," + str(second['lng']))
newlist.append("1")

with open('data.txt', 'w') as outfile:
    json.dump(newlist, outfile)

directions = gd.googledirections(first['lat'],first['lng'],second['lat'],second['lng'])

centroids=[]

ProbabilityOFPrintingRoute, RouteToPrint, AlternativeRoute, centroids= handler.Probability2(directions,y) #resolve the hard coding for two alternatives
print(RouteToPrint)
#print("############################################################################")
#print(RouteToPrint[2])
#print("############################################################################")
#print(RouteToPrint[AlternativeRoute])
