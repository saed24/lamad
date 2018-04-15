import sys

from flask import Flask, render_template, request, redirect, Response, jsonify, make_response
import random, json

app = Flask(__name__)

@app.route('/')
def output():
	# serve index template
	return render_template('index.html')

@app.route('/get_route')
def background_process():
    try:
        lang = request.args.get('request_type', 0, type=str)
        filepath = '1365683861651'
        routes = []
        with open(filepath) as fp:
            line = fp.readline()
            cnt = 1
            while line:
                points = {}
                line = fp.readline()
                temp = line.split(' ')
                
                if len(temp) == 4:
                    points['lat'] = float(temp[0])
                    points['lng'] = float(temp[1])
                    points['time'] = temp[2]
                    points['alt'] = temp[3]
                    print(points);
                    json_row = json.dumps(points)
                    routes.append(points)
               
        return jsonify(result=routes)	
    
    except Exception as e:
		   return str(e)

if __name__ == "__main__":
    app.run()