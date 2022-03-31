import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from scipy.sparse.construct import rand 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
import pickle

#classifier code

#loading the data
iris_dataset=load_iris()

#Splitting the data into features and label
x=iris_dataset["data"]
y=iris_dataset["target"]

#Splitting data into tarining and test data
x_train, x_test, y_train, y_test=train_test_split(x,y,random_state=0, test_size=0.3)

kclassifier=KNeighborsClassifier(n_neighbors=2)

#fitting training  data into KNN classifier
kclassifier.fit(x_train, y_train)


#Dumping the model into pickle
pickle.dump(kclassifier, open("model.pkl", "wb"))

model=pickle.load(open("model.pkl", "rb"))

xn=np.array([[7,3,4,1.5]])

xpred=kclassifier.predict(xn)

print(iris_dataset["target_names"][xpred])