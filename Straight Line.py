# -*- coding: utf-8 -*-
"""
Created on Thu May  3 11:50:49 2018

@author: Raheel
"""
import GridPy as gp
import googlemaps as gm

A={'lat': 62.618013, 'lng': 29.733355}
B={'lat': 62.615096, 'lng': 29.761848}

RouteToPrint=gp.doWGSInterpolation(A,B,4440)
