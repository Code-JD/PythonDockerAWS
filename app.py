from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def hello_world():
	return "Hello World!"

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

if __name__ == "__main__":
	# app.run(host="127.0.0.1", port=80)   for Production
	 app.run(debug=True),
