# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 18:27:18 2018

@author: Raheel
"""

def pointsToWGSCells(points, zoomLevel):
    cells = list()
    _map = {}
    prevCell = None
    for i,obj in enumerate(points):
        N = round(obj["lat"] * zoomLevel)
        E = round(obj["lng"] * zoomLevel)
        _id = str(E)+"-"+str(N)
        cell = {}
        cell["easting"] = E
        cell["northing"] = N
        cell["_id"] = _id
        cell["lat"] = E
        cell["lng"] = N
        cell["interpolation"] = 0
        if (prevCell != None):
            newCells = doWGSInterpolation(prevCell, cell, zoomLevel)
            for k,obj2 in enumerate(newCells):
                #print(newCells[k]['_id'])
                #print(cells)
                y=newCells[k]['_id']
                if y not in _map:
                    _map[y]=0
                if (_map[y]!= 1):
                    obj2["interpolation"] = 1
                    cells.append(obj2)
                    _map[obj2["_id"]] = 1
        if _id not in _map:
            _map[_id]=0
        if (_map[_id] != 1):
            _map[_id] = 1
            cells.append(cell)
        prevCell = cell
    #print(_map)
    return cells
	
def doWGSInterpolation(c1, c2, zoomLevel):
    minE = min(c1["easting"], c2["easting"])
    maxE = max(c1["easting"], c2["easting"])
    minN = min(c1["northing"], c2["northing"])
    maxN = max(c1["northing"], c2["northing"])
    deltaE = maxE - minE
    deltaN = maxN - minN
    cells = list()
    if (deltaN > deltaE):
        for i in range(minN, maxN):
            cell = {}
            cell["easting"] = c1["easting"] + round((c2["easting"] - c1["easting"]) * (i - c1["northing"]) / (c2["northing"] - c1["northing"]))
            cell["northing"] = i
            cell["lat"] = cell["northing"]
            cell["lng"] = cell["easting"]
            cell["_id"] = str(cell["easting"])+"-"+str(cell["northing"])
            cells.append(cell)
        
    else:
         for i in range(minE, maxE):
            cell = {}
            cell["easting"] = i
            cell["northing"] = c1["northing"] + round((c2["northing"] - c1["northing"]) * (i - c1["easting"]) / (c2["easting"] - c1["easting"]))
            cell["lat"] = cell["northing"]
            cell["lng"] = cell["easting"]
            cell["_id"] = str(cell["easting"])+"-"+str(cell["northing"])
            cells.append(cell)
            
    return cells

