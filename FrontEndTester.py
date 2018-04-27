# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 22:02:24 2018

@author: Raheel
"""

import frequency as f
import handler as handler
import googledirections as gd

y=f.addPointsToDict('1')

route=handler.readRouteFromFile('1216481888112')

outroute, first, second =handler.OuterRoute(route,2,99)


directions = gd.googledirections(first['lat'],first['lng'],second['lat'],second['lng'])

ProbabilityOFPrintingRoute, RouteToPrint, AlternativeRoute= handler.Probability(directions[0],directions[1],y)

#print(directions[1])
#directions[1]



print(ProbabilityOFPrintingRoute)