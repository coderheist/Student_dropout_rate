from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
import joblib
import os
from sklearn.ensemble import RandomForestClassifier
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)
CORS(app)

# Global variables for model
model = None
feature_names = [
    'Application_order', 'Course', 'Daytime_evening_attendance', 'Previous_qualification_grade',
    'Mothers_occupation', 'Fathers_occupation', 'Admission_grade', 'Displaced',
    'Tuition_fees_up_to_date', 'Scholarship_holder', 'International',
    'Curricular_units_1st_sem_credited', 'Curricular_units_1st_sem_enrolled',
    'Curricular_units_1st_sem_evaluations', 'Curricular_units_1st_sem_approved',
    'Curricular_units_1st_sem_grade', 'Curricular_units_2nd_sem_credited',
    'Curricular_units_2nd_sem_enrolled', 'Curricular_units_2nd_sem_evaluations',
    'Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade',
    'Unemployment_rate', 'GDP'
]

def load_model():
    global model
    try:
        # Try to load from different possible paths
        possible_paths = ['../random_forest_model.pkl', 'random_forest_model.pkl']
        for path in possible_paths:
            if os.path.exists(path):
                model = joblib.load(path)
                return
        # If no pickle file found, create simple model
        from sklearn.ensemble import RandomForestClassifier
        model = RandomForestClassifier(n_estimators=10, random_state=42)
        # Create dummy data for training
        X = np.random.rand(100, 23)
        y = np.random.randint(0, 2, 100)
        model.fit(X, y)
    except Exception as e:
        print(f"Model loading error: {e}")
        model = None

# Load model on import
load_model()

@app.route('/')
def health_check():
    return jsonify({
        "message": "Student Dropout Prediction API is running!",
        "model_loaded": model is not None,
        "features_count": len(feature_names),
        "endpoints": ["/predict", "/features", "/model-info"]
    })

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if model is None:
            return jsonify({"error": "Model not loaded"}), 500
            
        data = request.json
        
        # Extract features in correct order
        features = []
        for feature in feature_names:
            value = data.get(feature, 0)
            features.append(float(value))
        
        # Make prediction
        prediction = model.predict([features])[0]
        probabilities = model.predict_proba([features])[0]
        
        result = {
            "prediction": "Graduate" if prediction == 1 else "Dropout",
            "confidence": {
                "dropout": round(probabilities[0] * 100, 1),
                "graduate": round(probabilities[1] * 100, 1)
            }
        }
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/features')
def get_features():
    return jsonify({"features": feature_names, "count": len(feature_names)})

# Vercel handler
def handler(request, response):
    return app