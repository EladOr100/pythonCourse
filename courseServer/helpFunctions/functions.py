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
