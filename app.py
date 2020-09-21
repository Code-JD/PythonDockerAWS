from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def checkPostedData(postedData, functionName):
	if (functionName == "add" or functionName == "subtract" or functionName == "multiply"):
		if "x" not in postedData or "y" not in postedData:
			return 301 #Missing parameter
		else:
			return 200
	elif (functionName == "division"):
		if "x" not in postedData or "y" not in postedData:
			return 301
		elif int(postedData["y"]) == 0:
			return 302
		else:
			return 200

class Add(Resource):
	def post(self):
		# IF I am here, then the resource Add was requested using the method POST
		# Step 1: Get posted data:
		postedData = request.get_json()

		# Step 1b: Verify validity of a posted data
		status_code = checkPostedData(postedData, "add")
		if (status_code!=200):
			retJson = {
				"Message": "An error happened",
				"Status Code": status_code
			}
			return jsonify(retJson)
			
		# If I am here, then status_code == 200
		x = postedData["x"]
		y = postedData["y"]
		x = int(x)
		y = int(y)

		# Step 2: Add the posted data
		ret = x+y
		retMap = {
			"Message": ret,
			"Status Code": 200
		}		
		return jsonify(retMap)

class Subtract(Resource):
	def post(self):
		# IF I am here, then the resource Subtract was requested using the method POST
		# Step 1: Get posted data:
		postedData = request.get_json()

		# Step 1b: Verify validity of a posted data
		status_code = checkPostedData(postedData, "subtract")


		if (status_code!=200):
			retJson = {
				"Message": "An error happened",
				"Status Code": status_code
			}
			return jsonify(retJson)
			
		# If I am here, then status_code == 200
		x = postedData["x"]
		y = postedData["y"]
		x = int(x)
		y = int(y)

		# Step 2: Subtract the posted data
		ret = x-y
		retMap = {
			"Message": ret,
			"Status Code": 200
		}		
		return jsonify(retMap)

class Multiply(Resource):
	def post(self):
		# IF I am here, then the resource Multiply was requested using the method POST
		# Step 1: Get posted data:
		postedData = request.get_json()

		# Step 1b: Verify validity of a posted data
		status_code = checkPostedData(postedData, "multiply")


		if (status_code!=200):
			retJson = {
				"Message": "An error happened",
				"Status Code": status_code
			}
			return jsonify(retJson)
			
		# If I am here, then status_code == 200
		x = postedData["x"]
		y = postedData["y"]
		x = int(x)
		y = int(y)

		# Step 2: Multiply the posted data
		ret = x*y
		retMap = {
			"Message": ret,
			"Status Code": 200
		}		
		return jsonify(retMap)

class Divide(Resource):
	def post(self):
		# IF I am here, then the resource Subtract was requested using the method POST
		# Step 1: Get posted data:
		postedData = request.get_json()

		# Step 1b: Verify validity of a posted data
		status_code = checkPostedData(postedData, "division")


		if (status_code!=200):
			retJson = {
				"Message": "An error happened",
				"Status Code": status_code
			}
			return jsonify(retJson)
			
		# If I am here, then status_code == 200
		x = postedData["x"]
		y = postedData["y"]
		x = int(x)
		y = int(y)

		# Step 2: Divide the posted data
		ret = (x*1.0)/y
		retMap = {
			"Message": ret,
			"Status Code": 200
		}		
		return jsonify(retMap)

api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/division")

@app.route('/')
def hello_world():
	return "Hello World!"


"""
@app.route('/hithere')
def hi_there_everyone():
	return "I just hit /hithere"

@app.route('/add_two_nums', methods=["POST"])
def add_two_nums():
	#Get x,y from the posted date
	dataDict = request.get_json()

	if "y" not in dataDict:
		return "ERROR", 305 

	x = dataDict["x"]
	y = dataDict["y"]

	#Add z=x+y
	z = x+y

	#Prepare a JSON, "z":z
	retJSON = {
		"z": z
	}

	#Return jsonify(map_prepared)
	return jsonify(retJSON), 200

@app.route('/bye')
def bye():
	#Prepare a response for the request that came to /bye
	age = 2*5
	
	retJson = {
		'Name': 'Jonny',
		'Age': age,
		"phones": [
			{
				"phoneName": "Galaxy S10+",
				"phoneNumber": 5086236
			},
			{
				"phoneName": "Iphone10",
				"phoneNumber": 5313306
			}
		]
	}
	return jsonify(retJson)
"""

if __name__ == "__main__":
	# app.run(host="127.0.0.1", port=80)   for Production
	 app.run(debug=True),


# Comments have been added based on notes taken from video