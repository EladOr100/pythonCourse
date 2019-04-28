# importing the restRequests library
import requests
import json


def updateAgeInServer():
    URL = 'http://127.0.0.1:5000/getJsonData'
    r = requests.get(url=URL)
    data = json.loads(r.text)
    peopleLen = len(data['people'])
    for i in range(0, peopleLen):
        data['people'][i]['age'] = data['people'][i]['age'] + 1


def getAvarageAge():
    URL = 'http://127.0.0.1:5000/getJsonData'
    r = requests.get(url=URL)
    data = json.loads(r.text)
    peopleLen = len(data['people'])
    totalAges = 0
    for i in range(0, peopleLen):
        totalAges = totalAges + data['people'][i]['age']
    print("the avarge is {}".format(totalAges / peopleLen))


def getSkilesById(id):
    URL = 'http://127.0.0.1:5000/getJsonData'
    r = requests.get(url=URL)
    data = json.loads(r.text)
    peopleLen = len(data['people'])
    for i in range(0, peopleLen):
        if data['people'][i]['id'] == id:
            print("The user {} with the id {} has the next skill's {}".format(
                data['people'][i]['name'],
                id,
                data['people'][i]['programs']))


def sendGetRequest(url, path, query, name):
    # api-endpoint
    URL = url + path + query

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'name': name}
    # sending get request and saving the respons
    #  e as response object
    r = requests.get(url=URL, params=PARAMS)

    # extracting data format
    print("status code is: ", r.status_code)
    data = r.text
    print("return value is: ", data)


def get_my_name(url, path):
    URL = url + path
    r = requests.get(URL)
    print(r.text)


def get_json_data_and_print():
    r = requests.get('http://127.0.0.1:5000/getJsonDataTEST')
    print(r.text)


if __name__ == '__main__':
    get_json_data_and_print()
    url = 'http://127.0.0.1:5000/'
    path = 'my_name_is'
    get_my_name(url=url, path=path)
    # path = 'getname'
    # query = '?name=Elad'
    # name = 'Elad'
    # updateAgeInServer()
    # sendGetRequest(url=url, path=path, query=query, name=name)
    # getAvarageAge()
    # getSkilesById("046263422")
    # getSkilesById("200355479")
