# import some needed features
from flask import Flask, request, jsonify
from flask.logging import create_logger
import logging

# import some essential libraries
import pandas as pd
from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler

# define some other features
app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

# define "payload feature"
def scale(payload):
    """Scales Payload"""
    
    LOG.info("The scaled Payload: %s\n", payload)
    scaler = StandardScaler().fit(payload.astype(float))
    scaled_adhoc_predict = scaler.transform(payload.astype(float))
    return scaled_adhoc_predict

@app.route("/")
def home():
    html = f"<h3>The Sklearn - Housing price prediction in Boston </h3>"
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
    json_payload = request.json
    LOG.info("The created JSON payload is: %s", json_payload)
    inference_payload = pd.DataFrame(json_payload)
    LOG.info("The inference payload DataFrame is: %s", inference_payload)
    # create the final input with scaling
    scaled_payload = scale(inference_payload)
    # Collect the outputs of housing price prediction from the pretrained model, clf
    prediction = list(clf.predict(scaled_payload))
    # Write the final output of housing price prediction value
    LOG.info("The housing price prediction value is: %s", prediction)
    return jsonify({'prediction': prediction})

if __name__ == "__main__":
    # process the pretrained model with the name as clf
    clf = joblib.load("./model_data/boston_housing_prediction.joblib")
    app.run(host='0.0.0.0', port=80, debug=True) # specify port=80
