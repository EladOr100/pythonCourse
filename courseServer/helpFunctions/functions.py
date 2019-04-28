import json


def getJsonDataFromFile(jsonPath):
    with open(jsonPath) as f:
        data = json.load(f)
        return data


def writeToJson(jsonPath, data):
    with open(jsonPath, 'w') as outfile:
        json.dump(data, outfile, indent=4)


def getIdByName(name, data):
    for i in range(0, len(data['people'])):
        if data['people'][i]['name'] == name:
            id = data['people'][i]['id']
            print(id)
            return id


def updateFile(json_path, addToAdge):
    with open(json_path, 'r+') as f:
        data = json.load(f)
        for i in range(0, len(data['people'])):
            print(data['people'][i]['age'])
            data['people'][i]['age'] = data['people'][i]['age'] + int(addToAdge)
        f.seek(0)  # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()


def checkIfidExiest(req_data, db_json):
    for i in range(0, len(db_json)):
        if db_json['people'][i]['id'] == req_data['id']:
            return False
        return True
