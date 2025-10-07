import json

def handler(request, response):
    """
    Vercel serverless function for student dropout prediction
    Zero dependencies - uses only Python built-ins
    """
    
    # Set CORS headers
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Content-Type'] = 'application/json'
    
    # Handle preflight OPTIONS request
    if request.method == 'OPTIONS':
        response.status_code = 200
        return ''
    
    # Health check endpoint
    if request.method == 'GET':
        result = {
            "status": "API is running", 
            "message": "Student Dropout Prediction API",
            "version": "zero-dependencies"
        }
        response.status_code = 200
        return json.dumps(result)
    
    # Prediction endpoint
    if request.method == 'POST':
        try:
            # Get request data
            data = request.json if hasattr(request, 'json') and request.json else {}
            features = data.get('features', [])
            
            # Simple rule-based prediction
            if len(features) >= 23:
                try:
                    admission_grade = float(features[6]) if features[6] else 140
                    sem1_grade = float(features[14]) if features[14] else 12
                    sem2_grade = float(features[20]) if features[20] else 12
                except (ValueError, IndexError, TypeError):
                    admission_grade, sem1_grade, sem2_grade = 140, 12, 12
                
                # Simple scoring system
                score = 0
                if admission_grade > 150: score += 2
                elif admission_grade > 120: score += 1
                
                if sem1_grade > 14: score += 2
                elif sem1_grade > 10: score += 1
                
                if sem2_grade > 14: score += 2
                elif sem2_grade > 10: score += 1
                
                # Predict based on score
                if score >= 4:
                    prediction = 0  # Graduate
                    probability = 0.75 + (score - 4) * 0.05
                else:
                    prediction = 1  # Dropout
                    probability = 0.65 + (4 - score) * 0.05
                    
            else:
                # Default prediction if insufficient data
                prediction = 1
                probability = 0.50
            
            result = {
                'prediction': prediction,
                'probability': round(min(max(probability, 0.1), 0.9), 2),
                'message': 'Graduate' if prediction == 0 else 'At Risk of Dropout',
                'note': 'Rule-based prediction system'
            }
            
            response.status_code = 200
            return json.dumps(result)
            
        except Exception as e:
            error_response = {
                'error': f'Prediction failed: {str(e)}',
                'prediction': 1,
                'probability': 0.50,
                'message': 'At Risk of Dropout'
            }
            
            response.status_code = 500
            return json.dumps(error_response)
    
    # Method not allowed
    response.status_code = 405
    return json.dumps({'error': 'Method not allowed'})