from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np
from typing import Dict, Any, Union
import os

app = Flask(__name__)

model_path = os.path.join('models', 'model_1.pkl')

@app.route('/v1/predict/<Longitude>/<Latitude>', methods=["GET", "POST"])
def realtime(Longitude: float, Latitude: float) -> Dict[str, Any]:
    """
    Predict Irish with custom input data
    """
    # load saved pipeline object
    try:
        pipeline = joblib.load(model_path)
    except FileNotFoundError:
        return jsonify({'Error': 'Saved pipeline not found.'}), 404
    except Exception as e:
        return jsonify({'Error': f'Error loading pipeline: {str(e)}'}), 500

    # processing input data
    input_dict = {
        'Longitude': [float(Longitude)],
        'Latitude': [float(Latitude)],
    }
    data_input = pd.DataFrame(input_dict)
    result_dict = recommended_hospitals(pipeline, data_input)

    return jsonify(raw_data=input_dict, result=result_dict)

def recommended_hospitals(pipeline: Dict[str, object], input_data: pd.DataFrame) -> Dict[str, Union[str, float]]:
    """
    Predict the class and its probability for the given input data using the pipeline
    """
    # predict
    results = {}
    kmeans_model = pipeline  # Assuming the KMeans model is stored directly in the pipeline
    prediction = kmeans_model.predict(input_data)
    cluster_centers = kmeans_model.cluster_centers_
    
    # Add your logic here to process the prediction and cluster_centers
    
    return results

if __name__ == '__main__':
    app.run(debug=True, port=8080)
