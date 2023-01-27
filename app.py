# import some essential libraries
import pandas as pd
import numpy as np
import matplotlib as mp
import logging
# import some other components
from flask import Flask, jsonify, request
from sklearn.externals import joblib
from flask.logging import create_logger
from sklearn.preprocessing import StandardScaler

# define some other features
app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

# define "payload" features
def scale(payload):
    LOG.info("The Payload scaled is: %s\n", payload)
    sc = StandardScaler().fit(payload.astype(float))
    sc_predict = sc.transform(payload.astype(float))
    return sc_predict

@app.route("/")
def home():
    html = f"<h3>The Sklearn Prediction Home - Housing price prediction in Boston </h3>"
    return html.format(format)

@app.route("/predict", methods=['POST'])
def predict():
    """Performs an sklearn prediction
        input looks like:
        {
        "CHAS":{
        "0":0
        },
        "RM":{
        "0":6.575
        },
        "TAX":{
        "0":296.0
        },
        "PTRATIO":{
        "0":15.3
        },
        "B":{
        "0":396.9
        },
        "LSTAT":{
        "0":4.98
        }
        result looks like:
        { "prediction": [ <val> ] }
        
        """
    
    # Write the input of the payload
    j_load = request.json
    LOG.info("The created JSON payload is: %s", j_load)
    in_load = pd.DataFrame(j_load)
    LOG.info("The inference payload DataFrame is: %s", in_load)
    # create the final input with scaling
    scale_load = scale(in_load)
    # Collect the outputs of housing price prediction from the pretrained model, clf
    house_predict = list(clf.predict(scale_load))
    # Write the final output of housing price prediction value
    LOG.info("The housing price prediction value is: %s", house_predict)
    return jsonify({'prediction': house_predict})

if __name__ == "__main__":
    # process the pretrained model with the name as clf and use port 80 for implementing
    clf = joblib.load("./model_data/house_prediction.joblib")
    app.run(host='0.0.0.0', port=80, debug=True) 
