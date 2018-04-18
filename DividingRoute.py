# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 19:31:36 2018

@author: Raheel
"""

def DividingRoute(routes, A, B):
    A=int (len(routes)*(A/100))
    B=int (len(routes)*(B/100))
    return routes[A:B]