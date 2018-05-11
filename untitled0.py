# -*- coding: utf-8 -*-
"""
Created on Fri May 11 21:32:20 2018

@author: Raheel
"""


        
import frequency as f
import handler as handler
import sys

from flask import Flask, render_template, request, redirect, Response, jsonify, make_response
import random, json
import frequency as f
import handler as handler
import googledirections as gd
import GridPy as gp

y=f.addPointsToDict('1')

route=handler.readRouteFromFile('1216481888112')
A = 20
B = 90
#print(route)
outroute, first, second =handler.OuterRoute(route,A,B)
print("test1")
directions = gd.googledirections(first['lat'],first['lng'],second['lat'],second['lng'])
print("test2")
centroids=[]
print(directions)
ProbabilityOFPrintingRoute, RouteToPrint, AlternativeRoute, centroids= handler.Probability2(directions,y) #resolve the hard coding for two alternatives
print(ProbabilityOFPrintingRoute)
print(centroids)
print(AlternativeRoute)
print(RouteToPrint)
ProbabilityOFPrintingRoute, RouteToPrint, AlternativeRoute, centroids= handler.Probability(directions[0],directions[1],y) #resolve the hard coding for two alternatives
#print("test")
#print(centroids)