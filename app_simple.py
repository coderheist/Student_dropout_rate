#!/usr/bin/env python3
"""
Simple Student Dropout Prediction API - No Heavy Dependencies
Uses rule-based predictions when ML model fails to load
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json

app = Flask(__name__)
CORS(app)

def simple_prediction(features):
    """
    Rule-based prediction system as fallback
    Based on common dropout indicators
    """
    try:
        # Convert features to numeric values
        marital_status = float(features.get('marital_status', 1))
        application_mode = float(features.get('application_mode', 1))
        course = float(features.get('course', 9238))
        attendance = float(features.get('daytime_evening_attendance', 1))
        previous_qualification = float(features.get('previous_qualification', 1))
        nationality = float(features.get('nationality', 1))
        mothers_qualification = float(features.get('mothers_qualification', 1))
        fathers_qualification = float(features.get('fathers_qualification', 1))
        mothers_occupation = float(features.get('mothers_occupation', 1))
        fathers_occupation = float(features.get('fathers_occupation', 1))
        displaced = float(features.get('displaced', 0))
        educational_special_needs = float(features.get('educational_special_needs', 0))
        debtor = float(features.get('debtor', 0))
        tuition_fees = float(features.get('tuition_fees_up_to_date', 1))
        gender = float(features.get('gender', 1))
        scholarship_holder = float(features.get('scholarship_holder', 0))
        age_at_enrollment = float(features.get('age_at_enrollment', 20))
        international = float(features.get('international', 0))
        
        # Semester grades
        sem1_units_credited = float(features.get('curricular_units_1st_sem_credited', 0))
        sem1_grade = float(features.get('curricular_units_1st_sem_grade', 0))
        sem2_units_credited = float(features.get('curricular_units_2nd_sem_credited', 0))
        sem2_grade = float(features.get('curricular_units_2nd_sem_grade', 0))
        
        prev_units_approved = float(features.get('curricular_units_1st_sem_approved', 0))
        
        # Risk factors calculation
        risk_score = 0
        
        # Academic performance risk factors
        if sem1_grade < 10:  # Poor first semester grades
            risk_score += 3
        elif sem1_grade < 12:
            risk_score += 1
            
        if sem2_grade < 10:  # Poor second semester grades
            risk_score += 3
        elif sem2_grade < 12:
            risk_score += 1
            
        if sem1_units_credited < 4:  # Low credit completion
            risk_score += 2
            
        if sem2_units_credited < 4:
            risk_score += 2
        
        # Financial risk factors
        if tuition_fees == 0:  # Tuition not up to date
            risk_score += 2
            
        if debtor == 1:  # Student is a debtor
            risk_score += 1
        
        # Age risk factor
        if age_at_enrollment > 25:  # Older students higher dropout risk
            risk_score += 1
        elif age_at_enrollment > 30:
            risk_score += 2
        
        # Support factors (reduce risk)
        if scholarship_holder == 1:  # Has scholarship
            risk_score -= 1
            
        if sem1_grade > 15:  # Excellent grades
            risk_score -= 2
        elif sem1_grade > 13:  # Good grades
            risk_score -= 1
            
        # Determine prediction
        if risk_score >= 6:
            prediction = 1  # Dropout
            confidence = min(0.9, 0.6 + (risk_score - 6) * 0.1)
        elif risk_score >= 3:
            prediction = 0  # Enrolled but at risk
            confidence = 0.6 + (6 - risk_score) * 0.05
        else:
            prediction = 2  # Graduate
            confidence = min(0.9, 0.7 + (3 - risk_score) * 0.05)
        
        return {
            'prediction': int(prediction),
            'confidence': round(confidence, 3),
            'risk_factors': {
                'academic_performance': sem1_grade + sem2_grade,
                'financial_status': tuition_fees,
                'age_factor': age_at_enrollment,
                'support_systems': scholarship_holder
            },
            'model_used': 'rule_based_fallback'
        }
        
    except Exception as e:
        # Ultimate fallback
        return {
            'prediction': 0,
            'confidence': 0.5,
            'error': 'Using default prediction',
            'model_used': 'default_fallback'
        }

@app.route('/')
def home():
    return jsonify({
        'message': 'Student Dropout Prediction API',
        'status': 'active',
        'version': '2.0 - Simple Mode',
        'model': 'Rule-based prediction system',
        'endpoints': ['/predict']
    })

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Get prediction
        result = simple_prediction(data)
        
        # Map prediction to readable labels
        labels = {0: 'Enrolled', 1: 'Dropout', 2: 'Graduate'}
        result['prediction_label'] = labels.get(result['prediction'], 'Unknown')
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            'error': str(e),
            'prediction': 0,
            'prediction_label': 'Enrolled',
            'confidence': 0.5,
            'model_used': 'error_fallback'
        })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'model': 'simple_rule_based'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)