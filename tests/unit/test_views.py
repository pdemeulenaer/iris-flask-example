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
    
    
def test_api_predict(client):
    """
    GIVEN the model served in the app
    WHEN one row of data is sent
    THEN check that the app returns one value in ['setosa','versicolor','virginica']
    """    
    data = {
        'sepal length (cm)': 7,
        'sepal width (cm)': 3,
        'petal length (cm)': 4,
        'petal width (cm)': 1.5
    }
    url = '/api_predict'
    
    response = client.post(url, json=data)

    assert response.content_type == 'application/json'
    print(response.json)
    assert response.json in ['setosa','versicolor','virginica'] #== 'versicolor' or response.json == 'virginica'