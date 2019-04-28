from flask import Flask, render_template, send_from_directory
from flask import request
from helpFunctions import functions as fun
import json

app = Flask(__name__, static_url_path='')

json_path = '../files/data.json'


@app.route('/', methods=['GET'])  # GET requests
def hello_world():
    return 'Holla Amgio'


@app.route('/my_name_is', methods=['GET'])  # GET requests
def my_name_is():
    return 'Elad'


@app.route('/addPeople', methods=['POST'])  # POST requests json
def post_json_example():
    # req_data - get the json from the user
    req_data = request.get_json()
    # db_json - get the json data from db
    db_json = fun.getJsonDataFromFile(json_path)
    # add the user json to the db
    db_json['people'].append(req_data)
    name = req_data['name']
    id = req_data['id']
    kindergarten = req_data['education']['Kindergarten']
    programs = req_data['programs']
    canAdd = fun.checkIfidExiest(req_data, db_json)
    if canAdd:
        fun.writeToJson(json_path, db_json)
        return '''
               you add successfully the next object :
               The name is: {}
               The id value is: {}
               went to Kindergarten : {}
               The user know the next programs: {}
               '''.format(name, id, kindergarten, programs)
    else:
        return '''
                      you cant add {} he is already exist 
                      '''.format(id)


@app.route('/getname', methods=['GET'])  # GET requests query
def getIdByNameFromURL():
    # insert data into json
    data = fun.getJsonDataFromFile(json_path)
    # get id from json by name
    name = request.args.get('name')
    id = fun.getIdByName(name, data)
    return '''<h1>{} id value is: {}</h1>'''.format(name, id)


@app.route('/openweb', methods=['GET'])
def openweb():
    return render_template("index.html")


@app.route('/getJsonData', methods=['GET'])
def getJsonData():
    data = fun.getJsonDataFromFile(json_path)
    print(data)
    return json.dumps(data)


@app.route('/updateAge', methods=['GET'])
def updateAge():
    addToAdge = request.args.get('add')
    data = fun.getJsonDataFromFile(json_path)
    for i in range(0, len(data['people'])):
        print(data['people'][i]['age'])
        data['people'][i]['age'] = data['people'][i]['age'] + int(addToAdge)
    fun.writeToJson(json_path, data)
    return "ok add {} to all people".format(addToAdge)


@app.route('/getJsonDataTEST' ,methods=['GET'])
def getJsonDataTEST():
    with open('C:\\Users\\orela\\PycharmProjects\\courseServer\\files\\data.json') as file:
        data = json.load(file)
        return json.dumps(data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
