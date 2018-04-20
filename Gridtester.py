# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 19:29:35 2018

@author: Raheel
"""

import handler as handler
import GridPy as GridPy
        
routes = handler.readRouteFromFile()
#print(routes)

grid=GridPy.pointsToWGSCells(routes,4440)