from django.conf.urls import url
import requests
import json

URL = 'http://127.0.0.1:8000/stuapi/'


def get_deta(id=None):
    data = {}
    if id is not None:
        data = {'id': id}

    # dumps - used to convert python data to json data
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)

# get_deta(1)
# print('***')
# get_deta()


def post_data():
    data = {
        'name': 'rekha',
        'roll': '104',
        'city': 'Delhi'
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)

# post_data()


def update_data():
    data = {
        'id': 2,
        'name': 'Dev3',
        'city': 'Us'
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)

# update_data()


def delete_data():
    data = {
        'id': 4
    }
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)

delete_data()
