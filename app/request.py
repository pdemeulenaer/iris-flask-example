import requests
import json

# 1. For and INDIVIDUAL prediction (using /predict_api)
# Using CURL: TODO
# Using python request:
# url = 'http://localhost:5000/api_predict'
# data = requests.post(url,json={'sepal length (cm)': 7, 'sepal width (cm)': 3, 'petal length (cm)': 4, 'petal width (cm)': 1.5})
# print(data.json())


# 2. For a CSV file prediction (using /predict_api_file)
# Using CURL: curl -F "file=@data/iris_to_predict.csv" http://127.0.0.1:5000/api_predict_file (do this from the root of the repo)
# Using python request:
url = 'http://localhost:5000/api_predict_file'
files = {'file': ('report.csv', open('../data/iris_to_predict.csv', 'r'))}
data = requests.post(url, files=files)
print(data.json())



# '''
# data=[[7,3,4,1.5]]
# j_data = json.dumps(data)
# headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
# r = requests.post(url, data=j_data)
# print(r, r.text)
# '''

# import pandas as pd

# data = pd.read_csv("iris_to_predict.csv")
# print(data.head())
# print(data.shape)
# data_np = data.values
# print(data.shape)