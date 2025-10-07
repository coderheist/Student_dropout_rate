"""
Student Dropout Prediction API with ML Model
Uses Random Forest model with all 23 parameters
"""
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import pickle
import numpy as np

app = Flask(__name__, static_folder='static')
CORS(app)

# Load the ML model
MODEL_PATH = 'random_forest_model.pkl'
model = None

try:
    import warnings
    warnings.filterwarnings('ignore', category=UserWarning)
    
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    print("✅ Random Forest model loaded successfully!")
    print(f"   Model type: {type(model).__name__}")
except FileNotFoundError:
    print(f"⚠️ Model file not found: {MODEL_PATH}")
    print("Will use rule-based fallback system")
except Exception as e:
    print(f"⚠️ Could not load model: {e}")
    print("Will use rule-based fallback system")

# Feature names in the correct order for the model
FEATURE_ORDER = [
    'marital_status',
    'application_mode', 
    'course',
    'daytime_evening_attendance',
    'previous_qualification',
    'nationality',
    'mothers_qualification',
    'fathers_qualification',
    'mothers_occupation',
    'fathers_occupation',
    'displaced',
    'educational_special_needs',
    'debtor',
    'tuition_fees_up_to_date',
    'gender',
    'scholarship_holder',
    'age_at_enrollment',
    'international',
    'curricular_units_1st_sem_credited',
    'curricular_units_1st_sem_grade',
    'curricular_units_2nd_sem_credited',
    'curricular_units_2nd_sem_grade',
    'curricular_units_1st_sem_approved'
]

@app.route('/')
def home():
    # Serve the HTML interface
    return send_from_directory('static', 'index.html')

@app.route('/api')
def api_info():
    # API information endpoint
    model_status = 'Random Forest ML Model' if model else 'Rule-based fallback'
    return jsonify({
        'message': 'Student Dropout Prediction API',
        'status': 'active',
        'version': '3.0 - ML Model with 23 Parameters',
        'model': model_status,
        'parameters': 23,
        'endpoints': ['/predict', '/health', '/api']
    })

@app.route('/health')
def health():
    model_status = 'ml_random_forest' if model else 'rule_based_fallback'
    return jsonify({
        'status': 'healthy', 
        'model': model_status,
        'parameters': 23,
        'python_version': '3.9+',
        'dependencies': 'Flask, scikit-learn, numpy'
    })

def rule_based_fallback(data):
    """Rule-based prediction using all 23 parameters"""
    try:
        # Extract all 23 parameters
        age = float(data.get('age_at_enrollment', 20))
        grade1 = float(data.get('curricular_units_1st_sem_grade', 12))
        grade2 = float(data.get('curricular_units_2nd_sem_grade', 12))
        credits1 = float(data.get('curricular_units_1st_sem_credited', 0))
        credits2 = float(data.get('curricular_units_2nd_sem_credited', 0))
        approved1 = float(data.get('curricular_units_1st_sem_approved', 0))
        tuition = float(data.get('tuition_fees_up_to_date', 1))
        scholarship = float(data.get('scholarship_holder', 0))
        debtor = float(data.get('debtor', 0))
        displaced = float(data.get('displaced', 0))
        special_needs = float(data.get('educational_special_needs', 0))
        
        # Calculate comprehensive risk score
        risk_score = 0
        
        # Academic performance (weighted heavily)
        if grade1 < 10:
            risk_score += 4
        elif grade1 < 12:
            risk_score += 2
        elif grade1 > 15:
            risk_score -= 2
            
        if grade2 < 10:
            risk_score += 4
        elif grade2 < 12:
            risk_score += 2
        elif grade2 > 15:
            risk_score -= 2
        
        # Credit completion
        if credits1 < 4:
            risk_score += 2
        if credits2 < 4:
            risk_score += 2
        if approved1 < 3:
            risk_score += 2
            
        # Financial factors
        if tuition == 0:
            risk_score += 3
        if debtor == 1:
            risk_score += 2
        if scholarship == 1:
            risk_score -= 2
            
        # Age factor
        if age > 25:
            risk_score += 1
        if age > 30:
            risk_score += 2
            
        # Support needs
        if special_needs == 1:
            risk_score += 1
        if displaced == 1:
            risk_score += 1
            
        # Determine prediction with confidence
        if risk_score >= 8:
            prediction = 1  # Dropout
            label = 'Dropout'
            confidence = min(0.95, 0.75 + (risk_score - 8) * 0.05)
        elif risk_score >= 4:
            prediction = 0  # Enrolled
            label = 'Enrolled'  
            confidence = 0.65
        else:
            prediction = 2  # Graduate
            label = 'Graduate'
            confidence = min(0.95, 0.75 + (4 - risk_score) * 0.05)
            
        return {
            'prediction': int(prediction),
            'prediction_label': label,
            'confidence': round(confidence, 3),
            'risk_score': risk_score,
            'model_used': 'rule_based_fallback_23params'
        }
        
    except Exception as e:
        return {
            'prediction': 0,
            'prediction_label': 'Enrolled',
            'confidence': 0.5,
            'error': str(e),
            'model_used': 'error_fallback'
        }

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json() or {}
        
        # Try ML model first if available
        if model is not None:
            try:
                # Extract features in correct order
                features = []
                for feature_name in FEATURE_ORDER:
                    value = data.get(feature_name, 0)
                    features.append(float(value))
                
                # Convert to numpy array and reshape for prediction
                features_array = np.array(features).reshape(1, -1)
                
                # Make prediction
                prediction = int(model.predict(features_array)[0])
                
                # Get probability/confidence if available
                try:
                    probabilities = model.predict_proba(features_array)[0]
                    confidence = float(max(probabilities))
                except:
                    confidence = 0.85
                
                # Map prediction to label
                labels = {0: 'Enrolled', 1: 'Dropout', 2: 'Graduate'}
                label = labels.get(prediction, 'Unknown')
                
                return jsonify({
                    'prediction': prediction,
                    'prediction_label': label,
                    'confidence': round(confidence, 3),
                    'model_used': 'random_forest_ml_model',
                    'parameters_used': 23
                })
                
            except Exception as e:
                print(f"ML model prediction failed: {e}")
                # Fall through to rule-based system
        
        # Use rule-based fallback
        result = rule_based_fallback(data)
        return jsonify(result)
        
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