# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 11:00:58 2018

@author: Raheel
"""
import os    
import datetime

path = 'C:/Users/Raheel/PathPrediction/MopsiRoutes2014/routes/1/'
counter=0
routes = []

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
                #points['time'] = temp[2]
                points['alt'] = temp[3]
                timestamp, ms = divmod(int(temp[2]), 1000)
                points['time'] = datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')
                routes.append(points)

