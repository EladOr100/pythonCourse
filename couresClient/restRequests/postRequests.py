import requests
import json


def updateCource():
    data = {'programs':'python'}
    r = requests.post(url='http://127.0.0.1:5000/update_c', json=data)

def sendPostRequest(url, path, data):
    # api-endpoint
    URL = url + path
    # location given here
    print(data)
    # sending post request and saving the response as response object
    r = requests.post(url=URL, json=data)
    # extracting data format
    print("status code is: ", r.status_code)
    data = r.text
    print("return value is: ", data)


if __name__ == '__main__':
    json_path = '../files/person.json'
    url = 'http://127.0.0.1:5000/'
    path = 'addPeople'
    with open(json_path, 'r') as f:
        data = json.load(f)
    sendPostRequest(url, path, data=data)
r = requests.post('http://127.0.0.1:5000/', data={'key': 'value'})
