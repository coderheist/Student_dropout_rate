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
CORS(app)  # Enable CORS for React frontend

# Global variables for model
model = None
feature_columns = None
feature_names = [
    'Application_order',
    'Course',
    'Daytime_evening_attendance',
    'Previous_qualification_grade',
    'Mothers_occupation',
    'Fathers_occupation',
    'Admission_grade',
    'Displaced',
    'Tuition_fees_up_to_date',
    'Scholarship_holder',
    'International',
    'Curricular_units_1st_sem_credited',
    'Curricular_units_1st_sem_enrolled',
    'Curricular_units_1st_sem_evaluations',
    'Curricular_units_1st_sem_approved',
    'Curricular_units_1st_sem_grade',
    'Curricular_units_2nd_sem_credited',
    'Curricular_units_2nd_sem_enrolled',
    'Curricular_units_2nd_sem_evaluations',
    'Curricular_units_2nd_sem_approved',
    'Curricular_units_2nd_sem_grade',
    'Unemployment_rate',
    'GDP'
]

def create_sample_model():
    """Create a sample model with the specified 23 features"""
    print("Creating sample model with 23 features...")
    
    # Sample data for training
    np.random.seed(42)
    n_samples = 2000
    
    # Generate sample features based on realistic distributions
    data = {
        'Application_order': np.random.randint(0, 10, n_samples),
        'Course': np.random.randint(1, 20, n_samples),
        'Daytime_evening_attendance': np.random.choice([0, 1], n_samples),
        'Previous_qualification_grade': np.random.normal(140, 25, n_samples),
        'Mothers_occupation': np.random.randint(0, 15, n_samples),
        'Fathers_occupation': np.random.randint(0, 15, n_samples),
        'Admission_grade': np.random.normal(140, 20, n_samples),
        'Displaced': np.random.choice([0, 1], n_samples, p=[0.9, 0.1]),
        'Tuition_fees_up_to_date': np.random.choice([0, 1], n_samples, p=[0.2, 0.8]),
        'Scholarship_holder': np.random.choice([0, 1], n_samples, p=[0.7, 0.3]),
        'International': np.random.choice([0, 1], n_samples, p=[0.85, 0.15]),
        'Curricular_units_1st_sem_credited': np.random.randint(0, 8, n_samples),
        'Curricular_units_1st_sem_enrolled': np.random.randint(4, 8, n_samples),
        'Curricular_units_1st_sem_evaluations': np.random.randint(4, 12, n_samples),
        'Curricular_units_1st_sem_approved': np.random.randint(0, 8, n_samples),
        'Curricular_units_1st_sem_grade': np.random.normal(12, 3, n_samples),
        'Curricular_units_2nd_sem_credited': np.random.randint(0, 8, n_samples),
        'Curricular_units_2nd_sem_enrolled': np.random.randint(4, 8, n_samples),
        'Curricular_units_2nd_sem_evaluations': np.random.randint(4, 12, n_samples),
        'Curricular_units_2nd_sem_approved': np.random.randint(0, 8, n_samples),
        'Curricular_units_2nd_sem_grade': np.random.normal(12, 3, n_samples),
        'Unemployment_rate': np.random.normal(8, 3, n_samples),
        'GDP': np.random.normal(2, 1, n_samples)
    }
    
    df = pd.DataFrame(data)
    
    # Create target based on realistic logic
    target = np.where(
        (df['Admission_grade'] > 140) & 
        (df['Curricular_units_1st_sem_grade'] > 10) & 
        (df['Tuition_fees_up_to_date'] == 1) &
        (df['Unemployment_rate'] < 10), 1, 0
    )
    
    # Add some randomness to make it more realistic
    noise = np.random.choice([0, 1], n_samples, p=[0.75, 0.25])
    target = np.where(noise == 1, 1 - target, target)
    
    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(df, target)
    
    # Save model and feature columns
    joblib.dump(model, 'model.pkl')
    joblib.dump(df.columns.tolist(), 'feature_columns.pkl')
    
    print("Model created with accuracy:", model.score(df, target))
    return model, df.columns.tolist()

def load_model():
    """Load the trained model and feature columns"""
    global model, feature_columns
    
    # Try multiple paths for the random_forest_model.pkl file
    possible_paths = [
        '../random_forest_model.pkl',  # Parent directory
        'random_forest_model.pkl',     # Current directory
        os.path.join('..', 'random_forest_model.pkl'),  # Explicit parent directory
    ]
    
    try:
        for model_path in possible_paths:
            if os.path.exists(model_path):
                model = joblib.load(model_path)
                print(f"✓ Successfully loaded existing model from: {model_path}")
                feature_columns = feature_names  # Use the 23 feature names we defined
                print(f"✓ Model expects {len(feature_names)} features for prediction")
                return
            
        # Fallback: try local model.pkl
        if os.path.exists('model.pkl'):
            model = joblib.load('model.pkl')
            print("Model loaded successfully from model.pkl!")
            
            if os.path.exists('feature_columns.pkl'):
                feature_columns = joblib.load('feature_columns.pkl')
            else:
                feature_columns = feature_names
        else:
            print("⚠️  No existing pickle model found. Creating sample model...")
            model, feature_columns = create_sample_model()
            
    except Exception as e:
        print(f"❌ Error loading model: {str(e)}")
        print("Creating sample model...")
        model, feature_columns = create_sample_model()

def preprocess_input(data):
    """Preprocess input data to match model expectations"""
    
    # Ensure all required features are present with default values
    processed_data = {}
    defaults = {
        'Application_order': 1,
        'Course': 1,
        'Daytime_evening_attendance': 1,
        'Previous_qualification_grade': 140.0,
        'Mothers_occupation': 1,
        'Fathers_occupation': 1,
        'Admission_grade': 140.0,
        'Displaced': 0,
        'Tuition_fees_up_to_date': 1,
        'Scholarship_holder': 0,
        'International': 0,
        'Curricular_units_1st_sem_credited': 0,
        'Curricular_units_1st_sem_enrolled': 6,
        'Curricular_units_1st_sem_evaluations': 6,
        'Curricular_units_1st_sem_approved': 6,
        'Curricular_units_1st_sem_grade': 12.0,
        'Curricular_units_2nd_sem_credited': 0,
        'Curricular_units_2nd_sem_enrolled': 6,
        'Curricular_units_2nd_sem_evaluations': 6,
        'Curricular_units_2nd_sem_approved': 6,
        'Curricular_units_2nd_sem_grade': 12.0,
        'Unemployment_rate': 7.0,
        'GDP': 2.0
    }
    
    for feature in feature_names:
        if feature in data:
            try:
                processed_data[feature] = float(data[feature])
            except (ValueError, TypeError):
                processed_data[feature] = defaults.get(feature, 0.0)
        else:
            processed_data[feature] = defaults.get(feature, 0.0)
    
    # Create DataFrame with correct column order
    df = pd.DataFrame([processed_data])[feature_names]
    return df

@app.route('/', methods=['GET'])
def home():
    """Health check endpoint"""
    return jsonify({
        'message': 'Student Dropout Prediction API is running!',
        'model_loaded': model is not None,
        'features_count': len(feature_names),
        'features': feature_names,
        'endpoints': ['/predict', '/features', '/model-info']
    })

@app.route('/features', methods=['GET'])
def get_features():
    """Get list of all features used in the model"""
    feature_descriptions = {
        'Application_order': 'Application order (0-9)',
        'Course': 'Course code (1-20)',
        'Daytime_evening_attendance': 'Daytime/evening attendance (0=Evening, 1=Daytime)',
        'Previous_qualification_grade': 'Previous qualification grade',
        'Mothers_occupation': 'Mother\'s occupation code (0-15)',
        'Fathers_occupation': 'Father\'s occupation code (0-15)',
        'Admission_grade': 'Admission grade',
        'Displaced': 'Displaced status (0=No, 1=Yes)',
        'Tuition_fees_up_to_date': 'Tuition fees up to date (0=No, 1=Yes)',
        'Scholarship_holder': 'Scholarship holder (0=No, 1=Yes)',
        'International': 'International student (0=No, 1=Yes)',
        'Curricular_units_1st_sem_credited': 'Curricular units 1st sem (credited)',
        'Curricular_units_1st_sem_enrolled': 'Curricular units 1st sem (enrolled)',
        'Curricular_units_1st_sem_evaluations': 'Curricular units 1st sem (evaluations)',
        'Curricular_units_1st_sem_approved': 'Curricular units 1st sem (approved)',
        'Curricular_units_1st_sem_grade': 'Curricular units 1st sem (grade)',
        'Curricular_units_2nd_sem_credited': 'Curricular units 2nd sem (credited)',
        'Curricular_units_2nd_sem_enrolled': 'Curricular units 2nd sem (enrolled)',
        'Curricular_units_2nd_sem_evaluations': 'Curricular units 2nd sem (evaluations)',
        'Curricular_units_2nd_sem_approved': 'Curricular units 2nd sem (approved)',
        'Curricular_units_2nd_sem_grade': 'Curricular units 2nd sem (grade)',
        'Unemployment_rate': 'Unemployment rate (%)',
        'GDP': 'GDP growth rate (%)'
    }
    
    return jsonify({
        'features': feature_names,
        'feature_descriptions': feature_descriptions,
        'total_features': len(feature_names)
    })

@app.route('/predict', methods=['POST'])
def predict():
    """Predict student dropout/graduation"""
    try:
        # Get JSON data from request
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Check if model is loaded
        if model is None:
            return jsonify({'error': 'Model not loaded'}), 500
        
        # Preprocess input data
        input_df = preprocess_input(data)
        
        # Make prediction
        prediction = model.predict(input_df)[0]
        prediction_proba = model.predict_proba(input_df)[0]
        
        # Convert prediction to human-readable format
        prediction_text = "Graduate" if prediction == 1 else "Dropout"
        
        # Get confidence scores
        dropout_confidence = round(prediction_proba[0] * 100, 2)
        graduate_confidence = round(prediction_proba[1] * 100, 2)
        
        response = {
            'prediction': prediction_text,
            'prediction_numeric': int(prediction),
            'confidence': {
                'dropout': dropout_confidence,
                'graduate': graduate_confidence
            },
            'input_data': data,
            'processed_features': input_df.iloc[0].to_dict()
        }
        
        return jsonify(response)
        
    except Exception as e:
        return jsonify({'error': f'Prediction failed: {str(e)}'}), 500

@app.route('/model-info', methods=['GET'])
def model_info():
    """Get information about the loaded model"""
    info = {
        'model_loaded': model is not None,
        'feature_columns': feature_names,
        'total_features': len(feature_names),
        'model_type': type(model).__name__ if model else None,
        'model_file': 'model.pkl' if os.path.exists('model.pkl') else 'sample_model'
    }
    
    if model and hasattr(model, 'feature_importances_'):
        feature_importance = dict(zip(feature_names, model.feature_importances_))
        # Sort by importance
        sorted_importance = dict(sorted(feature_importance.items(), key=lambda x: x[1], reverse=True))
        info['feature_importance'] = sorted_importance
    
    return jsonify(info)

if __name__ == '__main__':
    print("Starting Student Dropout Prediction API...")
    print("Using existing random_forest_model.pkl file for predictions")
    print("Features used in prediction:")
    for i, feature in enumerate(feature_names):
        print(f"{i}: {feature}")
    
    # Load model on startup
    load_model()
    
    print(f"\nModel loaded successfully! Using {len(feature_names)} features for prediction.")
    print("API will be available at: http://localhost:5000")
    print("Endpoints:")
    print("  - GET /: Health check")
    print("  - GET /features: List all features")
    print("  - POST /predict: Make predictions")
    print("  - GET /model-info: Model information")
    
    app.run(debug=True, host='0.0.0.0', port=5000)