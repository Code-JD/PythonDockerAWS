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
	dateDict = request.get_json()
	return jsonify(dataDict)
	#Add z=x+y

	#Prepare a JSON, "z":z

	#Return jsonify(map_prepared)

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
