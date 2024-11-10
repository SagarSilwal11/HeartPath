# patient/prediction_model.py

import pandas as pd
import pickle
import os

def predict_heart_disease(patient_data):
    # Convert incoming data to a DataFrame (for model prediction)
    data = pd.DataFrame([{
        'Age': patient_data['age'],
        'Sex': patient_data['sex'],
        'ChestPainType': patient_data['chestpain'],
        'RestingBP': patient_data['restingbp'],
        'Cholesterol': patient_data['cholesterol'],
        'FastingBS': patient_data['fastingbs'],
        'RestingECG': patient_data['restingecg'],
        'MaxHR': patient_data['maxhr'],
        'ExerciseAngina': patient_data['exerciseangina'],
        'Oldpeak': patient_data['oldpeak'],
        'ST_Slope': patient_data['st_slope']
    }])

    # Correct way to load the model using a relative path
    model_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'model.pkl')
    
    # Load the trained model
    with open(model_path, 'rb') as file:
        model = pickle.load(file)

    # Make the prediction
    result = model.predict(data)
    
    # Return a prediction label (this could be more specific based on the model output)
    if result == 0:
        return "No Heart Disease"
    else:
        return "Heart Disease Present"
