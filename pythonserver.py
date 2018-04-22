import sys

from flask import Flask, render_template, request, redirect, Response, jsonify, make_response
import random, json
import handler as handler
import osrm as osrm

app = Flask(__name__)

@app.route('/')
def output():
	# serve index template
	return render_template('index.html')

@app.route('/get_route')
def returnRoute():
    try:
        lang = request.args.get('request_type', 0, type=str)
      
       # startPoint = {'lat': '60.1699', 'lng': '24.9384'}
        #endPoint = {'lat': '60.2055', 'lng': '24.6559'}
        
        #routes = osrm.getRoutesFromOSRM(startPoint, endPoint, "driving")
        routes= handler.readRouteFromFile('1218616715718')
        print(routes)
        
        return jsonify(result=routes)	
    
    except Exception as e:
		   return str(e)

if __name__ == "__main__":
    app.run()