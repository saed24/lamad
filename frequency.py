# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 19:29:35 2018

@author: Raheel
"""

import handler as handler
import GridPy as GridPy
import os


def addToDict(dicts,grid):
    for x in range(0, len(grid)):
        if(grid[x]['_id'] not in dicts):
            dicts[grid[x]['_id']] = 1
            
        elif(grid[x]['_id'] in dicts):
            dicts[grid[x]['_id']] += 1
    

def addPointsToDict(user):
    path = './MopsiRoutes2014/routes/'+user
    dicts = {}
    for filename in os.listdir(path):
        route = handler.readRouteFromFile(path+filename)
        
        grid=GridPy.pointsToWGSCells(route,111)
        addToDict(dicts, grid)
    
    return dicts

print(addPointsToDict())
        




    




