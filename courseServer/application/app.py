from flask import Flask
from flask import request
from helpFunctions import functions as fun

app = Flask(__name__)

json_path = '../files/data.json'


@app.route('/', methods=['GET'])  # GET requests
def hello_world():
    return 'Hello World! {}'


@app.route('/addPeople', methods=['POST'])  # POST requests json
def post_json_example():
    # req_data - get the json from the user
    req_data = request.get_json()
    # db_json - get the json data from db
    db_json = fun.getJsonDataFromFile(json_path)
    # add the user json to the db
    db_json['people'].append(req_data)
    fun.writeToJson(json_path, db_json)
    name = req_data['name']
    id = req_data['id']
    kindergarten = req_data['education']['Kindergarten']
    programs = req_data['programs']

    return '''
           you add successfully the next object :
           The name is: {}
           The id value is: {}
           went to Kindergarten : {}
           The user know the next programs: {}
           '''.format(name, id, kindergarten, programs)


@app.route('/getname', methods=['GET'])  # GET requests query
def getIdByNameFromURL():
    # insert data into json
    data = fun.getJsonDataFromFile(json_path)
    # get id from json by name
    name = request.args.get('name')
    id = fun.getIdByName(name, data)
    return '''<h1>{} id value is: {}</h1>'''.format(name, id)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
