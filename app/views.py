'''
This module contains the Flask app views
'''

import pickle
import numpy as np 
import pandas as pd
from flask import request, jsonify, render_template
from app import app


# Model upload (should it be done here or within the relevant functions below?)
model = pickle.load(open("model/model.pkl", "rb"))


@app.route('/')
def home():
    '''
    Home html rendering in Flask app
    '''
    return render_template('index.html')


@app.route("/about")
def about():
    '''
    Test function in Flask app
    '''
    return "All about Flask"


@app.route('/predict', methods=['POST'])
def predict():
    '''
    This function allows direct prediction in the GUI
    '''
    initial_features = [float(x) for x in request.form.values()]
    final_features = [np.array(initial_features)]
    predictions = model.predict(final_features)
    species = ['Setosa','Versicolor','Virginica']
    output = species[predictions[0]]
    return render_template('index.html', prediction_species="The Predicted Species is {}".format(output))


@app.route('/api_predict', methods=["POST"])
def api_predict():
    '''
    This api allows user to POST a request for an individual entry
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])
    species = ['setosa','versicolor','virginica']
    output = species[prediction[0]]
    return jsonify(output)


@app.route('/api_predict_file', methods=["POST"])
def api_predict_file():
    '''
    This api allows user to POST a request for multiple entries, posted in a CSV file
    '''    
    data = pd.read_csv(request.files.get("file"))
    prediction = model.predict(data)
    # species = ['setosa','versicolor','virginica']
    return str(list(prediction))    
