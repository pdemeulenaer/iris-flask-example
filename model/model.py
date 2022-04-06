"""
Simple KNN classification of Iris dataset.
Purpose is to produce the pickle artefact that can be used in the Flask app
"""

import pickle
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, roc_auc_score

# Data loading
iris_dataset = load_iris()
x = iris_dataset["data"]
y = iris_dataset["target"]

# Train, Test split
x_train, x_test, y_train, y_test = train_test_split(x,y,random_state=0, test_size=0.3)

# Model declaration and fitting
clf = KNeighborsClassifier(n_neighbors=2)
clf.fit(x_train, y_train)

# Performance metric
y_pred = clf.predict(x_test)
acc = accuracy_score(y_test, y_pred)
print ('acc:',acc)

# Saving the model artifact locally
pickle.dump(clf, open("model.pkl", "wb"))

# Model loading for simple testing on dummy data
model = pickle.load(open("model.pkl", "rb"))
data = np.array([[2,8,1,3]])
predictions = model.predict(data)
print(iris_dataset["target_names"][predictions])
