# importing the restRequests library
import requests


def sendGetRequest(url, path, query, name):
    # api-endpoint
    URL = url + path + query

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'name': name}
    # sending get request and saving the response as response object
    r = requests.get(url=URL, params=PARAMS)

    # extracting data format
    print("status code is: ", r.status_code)
    data = r.text
    print("return value is: ", data)


if __name__ == '__main__':
    url = 'http://127.0.0.1:5000/'
    path = 'getname'
    query = '?name=Elad'
    name = 'Elad'
    sendGetRequest(url=url, path=path, query=query, name=name)
