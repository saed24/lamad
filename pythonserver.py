import sys

from flask import Flask, render_template, request, redirect, Response, jsonify, make_response
import random, json
import handler as handler
import osrm as osrm
import frequency as f

app = Flask(__name__)
filenames = ['1216464589688','1216468520320','1216481888112']


@app.route('/')
def output():
    #f.addPointsToDict('13')
	# serve index template

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
    try:
        routeSel = request.args.get('route', 0, type=str)
        
        routeSel = int(routeSel)
        print(routeSel)
        
        route = []
        
        if(routeSel == 1):
            print(filenames[0])
            route = handler.readRouteFromFile(filenames[0])
        
        elif(routeSel == 2):
            route = handler.readRouteFromFile(filenames[1])
            
        elif(routeSel == 3):
            route = handler.readRouteFromFile(filenames[2])
        
        return jsonify(result=route)	
    
    except Exception as e:
		   return str(e)
       

if __name__ == "__main__":
    app.run()