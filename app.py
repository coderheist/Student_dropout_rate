"""
Direct Simple App for Render - No subdirectories
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({
        'message': 'Student Dropout Prediction API (Simple Version)',
        'status': 'active',
        'version': '2.0 - Direct Deploy',
        'model': 'Rule-based prediction system',
        'endpoints': ['/predict', '/health']
    })

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy', 
        'model': 'simple_rule_based',
        'python_version': '3.9+',
        'dependencies': 'Flask only'
    })

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json() or {}
        
        # Simple rule-based prediction
        risk_score = 0
        
        # Get key risk factors
        age = float(data.get('age_at_enrollment', 20))
        grade1 = float(data.get('curricular_units_1st_sem_grade', 12))
        grade2 = float(data.get('curricular_units_2nd_sem_grade', 12))
        tuition = float(data.get('tuition_fees_up_to_date', 1))
        scholarship = float(data.get('scholarship_holder', 0))
        debtor = float(data.get('debtor', 0))
        
        # Calculate risk
        if grade1 < 10 or grade2 < 10:
            risk_score += 3
        if age > 25:
            risk_score += 2
        if tuition == 0:
            risk_score += 2
        if debtor == 1:
            risk_score += 1
        if scholarship == 1:
            risk_score -= 1
            
        # Determine prediction
        if risk_score >= 5:
            prediction = 1  # Dropout
            label = 'Dropout'
            confidence = 0.8
        elif risk_score >= 2:
            prediction = 0  # Enrolled
            label = 'Enrolled'  
            confidence = 0.7
        else:
            prediction = 2  # Graduate
            label = 'Graduate'
            confidence = 0.75
            
        return jsonify({
            'prediction': prediction,
            'prediction_label': label,
            'confidence': confidence,
            'risk_score': risk_score,
            'model_used': 'simple_rule_based_v2'
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e),
            'prediction': 0,
            'prediction_label': 'Enrolled',
            'confidence': 0.5,
            'model_used': 'error_fallback'
        }), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    print(f"Starting app on port {port}")
    app.run(host='0.0.0.0', port=port, debug=False)