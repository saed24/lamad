import sys

from flask import Flask, render_template, request, redirect, Response, jsonify, make_response
import random, json
import frequency as f
import handler as handler
import googledirections as gd
import GridPy as gp

app = Flask(__name__)
filenames = ['1216464589688','1216468520320','1216481888112']
route = []
y=f.addPointsToDict('1')

@app.route('/')
def output():
    
    
    return render_template('index.html')

@app.route('/get_route')
def returnRoute():
    try:
        lang = request.args.get('request_type', 0, type=str)
      
        print(lang)
       # startPoint = {'lat': '60.1699', 'lng': '24.9384'}
        #endPoint = {'lat': '60.2055', 'lng': '24.6559'}
        
        #routes = osrm.getRoutesFromOSRM(startPoint, endPoint, "driving")
        routes= handler.readRouteFromFile('1218625425687')
        print(routes)
        
        return jsonify(result=routes)	
    
    except Exception as e:
		   return str(e)


@app.route('/select_route')
def selectRoute():
    global route
    
    try:
        routeSel = request.args.get('route', 0, type=str)
        
        routeSel = int(routeSel)
        #print(routeSel)

        if(routeSel == 1):
           
            route = handler.readRouteFromFile(filenames[0])
        
        elif(routeSel == 2):
            route = handler.readRouteFromFile(filenames[1])
            
        elif(routeSel == 3):
            route = handler.readRouteFromFile(filenames[2])
        
        return jsonify(result=route)	
    
    except Exception as e:
		   return str(e)
       
        
@app.route('/predict_route')
def predictRoute():
    global y
    
    try:
        A = request.args.get('A', 0, type=str)
        B = request.args.get('B', 0, type=str)
        #print(A)
        #print(B)
        
        A = int(A)
        B = int(B)
        #print(route)
        outroute, first, second =handler.OuterRoute(route,A,B)
        #print("test")
        directions = gd.googledirections(first['lat'],first['lng'],second['lat'],second['lng'])
        #print("test")
        centroids=[]
        ProbabilityOFPrintingRoute, RouteToPrint, AlternativeRoute, centroids= handler.Probability(directions[0],directions[1],y) #resolve the hard coding for two alternatives
        #print("test")
        #print(centroids)
        linear= []
        linear.append(first)
        linear.append(second)
        #RouteToPrint=gp.doWGSInterpolation(A,B,4440)
        return jsonify(probability=ProbabilityOFPrintingRoute, routePrint=RouteToPrint, altRoute=AlternativeRoute, start=linear,centroids=centroids)	
    
    except Exception as e:
        print("exception")
        return str(e)

if __name__ == "__main__":
    app.run()