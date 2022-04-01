import pytest
import json
from app import app


def test_home(client):
    resp = client.get('/')
    assert resp.status_code == 200
    # assert isinstance(resp.json, dict)
    # assert resp.json.get('message', 'Hello Flask')


def test_home_bad_http_method(client):
    resp = client.post('/')
    assert resp.status_code == 405
    
    
def test_about(client):
    resp = client.get('/about')
    assert resp.status_code == 200
    # assert isinstance(resp.json, dict)
    # assert resp.json.get('message', 'All about Flask') 
    
    
def test_predict(client):
    data = {
        'sepal length (cm)': 7,
        'sepal width (cm)': 3,
        'petal length (cm)': 4,
        'petal width (cm)': 1.5
    }
    url = '/predict'
    # url = 'http://localhost:5000/api_predict'
    # data = requests.post(url,json={'sepal length (cm)': 7, 'sepal width (cm)': 3, 'petal length (cm)': 4, 'petal width (cm)': 1.5})

    response = client.post(url, data=json.dump(data))

    assert response.content_type == 'application/json'
    assert response.json['Result'] == 'versicolor'    