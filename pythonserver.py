import sys

from flask import Flask, render_template, request, redirect, Response, jsonify, make_response
import random, json
import handler as handler

app = Flask(__name__)

@app.route('/')
def output():
	# serve index template
	return render_template('index.html')

@app.route('/get_route')
def returnRoute():
    try:
        lang = request.args.get('request_type', 0, type=str)
        
        routes = handler.readRouteFromFile()
        routes2 = handler.readRoutesFromFolder()
        print(routes2[100])
        
        return jsonify(result=routes)	
    
    except Exception as e:
		   return str(e)

if __name__ == "__main__":
    app.run()