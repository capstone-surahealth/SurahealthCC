from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np
from typing import Dict, Any, Union

app = Flask(__name__)

@app.route('/v1/predict/<Longitude>/<Latitude>', methods=["GET", "POST"])
def realtime(Longitude: float, Latitude: float) -> Dict[str, Any]:
    """
    Predict Irish with custom input data
    """
    # load saved pipeline object
    try:
        pipeline = joblib.load('models/model_1.pkl')
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
    Predict the class and its probability for each model in the given pipeline
    """
    # predict
    results = {}
    for model_name, model in pipeline.items():
        if not model_name.startswith('model_'):
            continue
        prediction = model.predict(input_data)
        probas = np.max(model.predict_proba(input_data)[0]) * 100
        encoder = pipeline['label_encoder']
        results[f"{type(model).__name__}'s Prediction"] = f'{probas:.2f}% is {encoder.inverse_transform([prediction])[0]}'
    return results

if __name__ == '__main__':
    app.run(debug=True, port=8080)
