# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 00:30:11 2018

@author: Raheel
"""

import frequency as f
import handler as handler
import GridPy as grid

y=f.addPointsToDict('13')

route=handler.readRouteFromFile('1372602289525')
route2=handler.readRouteFromFile('1372604194383')

grid_1=grid.pointsToWGSCells(route,4440)
grid_2=grid.pointsToWGSCells(route2,4440)


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
       # print(counter2)
        
       
base=counter1+counter2       

counter1=round((counter1/base)*100)
counter2=round((counter2/base)*100)

#for x in range(0, len(dict1)):
#    if(dict1[x]['key'] in y):
 #       print('now')
        
        
'''for key, value in y:
    for key2, value2 in dict1:
        if key2==key:
            print('something')'''