import pytest
import json
import io
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
    GIVEN the model served in the app for unique item through the api api_predict
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
    
    

def test_api_predict_file(client):
    '''
    GIVEN the model served in the app for multiple items served in a CSV file to the api_predict_file api
    WHEN one such CSV of data is sent
    THEN check that the app returns one value in ['setosa','versicolor','virginica']    
    '''
    data = {
        'field': 'value',
        'file': (io.BytesIO(b'5.1,3.5,1.4,0.2\n 5.1,3.5,1.4,0.2\n'), 'test.csv')
    }
    
    # data = dict(file=(io.BytesIO(b"5.1,3.5,1.4,0.2"), 'test.csv'),)
    
    # url = 'http://localhost:5000/api_predict_file'
    # files = {'file': ('report.csv', open('../data/iris_to_predict.csv', 'r'))}
    files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}
    # data = requests.post(url, files=files)    

    rv = client.post('/api_predict_file', 
                    buffered=True, 
                    content_type='multipart/form-data', 
                    data=data, 
                    follow_redirects=True)
    
    assert rv.status_code == 200 
    # assert TODO: check that the answers are in the ['setosa','versicolor','virginica'] solution