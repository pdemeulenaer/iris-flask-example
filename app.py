from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np 
import pandas as pd



app=Flask(__name__)
model=pickle.load(open("model.pkl", "rb"))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
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
    species = ['setosa','versicolor','virginica']
    return str(list(prediction))


if __name__ == "__main__":
    app.run(debug=True)