# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 16:08:39 2018

@author: Raheel
"""

import handler as handler
import Distance as Distance
import DividingRoute as DividingRoute

routes = handler.readRouteFromFile()
total_distance=Distance.PathDistance(routes)
print(total_distance)

Div_route=DividingRoute.DividingRoute(routes,1,100)