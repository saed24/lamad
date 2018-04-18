# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 16:08:39 2018

@author: Raheel
"""

import handler as handler
import Distance as Distance

routes = handler.readRouteFromFile()
total_distance=Distance.PathDistance(routes)
print(total_distance)


print(len(routes))

print(routes[:5])
print list1[-5:]