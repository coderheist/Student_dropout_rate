from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import json
import os

app = Flask(__name__)
CORS(app)

# Feature names for the ML model
FEATURE_NAMES = [
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

# Simple rule-based prediction (for demo purposes when ML model unavailable)
def simple_predict(features):
    """Simple rule-based prediction for demonstration"""
    try:
        # Extract key features
        admission_grade = features[6] if len(features) > 6 else 140
        sem1_grade = features[14] if len(features) > 14 else 12
        sem2_grade = features[20] if len(features) > 20 else 12
        tuition_paid = features[8] if len(features) > 8 else 1
        unemployment = features[21] if len(features) > 21 else 8
        
        # Simple scoring logic
        score = 0
        
        # Academic performance (40% weight)
        if admission_grade > 150: score += 0.2
        if sem1_grade > 14: score += 0.1
        if sem2_grade > 14: score += 0.1
        
        # Financial stability (30% weight)
        if tuition_paid == 1: score += 0.15
        if unemployment < 8: score += 0.15
        
        # Base probability
        score += 0.3
        
        # Convert to binary prediction
        prediction = 1 if score > 0.6 else 0
        confidence_grad = min(max(score, 0.1), 0.9)
        confidence_drop = 1 - confidence_grad
        
        return prediction, [confidence_drop, confidence_grad]
        
    except Exception as e:
        # Fallback prediction
        return 1, [0.4, 0.6]

@app.route('/')
def health_check():
    return jsonify({
        "message": "Student Dropout Prediction API is running!",
        "model_type": "Rule-based prediction system",
        "features_count": len(FEATURE_NAMES),
        "endpoints": ["/predict", "/features", "/model-info"],
        "features": FEATURE_NAMES[:5]  # Show first 5 features
    })

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        # Extract features in correct order
        features = []
        for feature in FEATURE_NAMES:
            value = data.get(feature, 0)
            try:
                features.append(float(value))
            except (ValueError, TypeError):
                features.append(0.0)
        
        # Make prediction using simple rule-based system
        prediction, probabilities = simple_predict(features)
        
        result = {
            "prediction": "Graduate" if prediction == 1 else "Dropout",
            "confidence": {
                "dropout": round(probabilities[0] * 100, 1),
                "graduate": round(probabilities[1] * 100, 1)
            },
            "model_info": "Rule-based prediction system",
            "features_processed": len(features)
        }
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            "error": str(e),
            "message": "Prediction failed - using default values"
        }), 400

@app.route('/features', methods=['GET'])
def get_features():
    return jsonify({
        "features": FEATURE_NAMES,
        "count": len(FEATURE_NAMES),
        "description": "23 parameters for student dropout prediction"
    })

@app.route('/model-info', methods=['GET'])
def model_info():
    return jsonify({
        "model_type": "Rule-based prediction system",
        "features": len(FEATURE_NAMES),
        "output": "Binary classification (Dropout=0, Graduate=1)",
        "confidence": "Probability scores for each class"
    })

# Vercel serverless function handler
def handler(request, context):
    return app

# Export the app for Vercel
app_handler = app