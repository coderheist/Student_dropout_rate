"""
Ultra-minimal Vercel serverless function for student dropout prediction
Uses built-in Python only - no external dependencies
"""

def handler(request):
    """Minimal HTTP handler for Vercel"""
    
    # Handle CORS preflight
    if request.method == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type',
            }
        }
    
    # Health check
    if request.method == 'GET':
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': '{"status": "API is running", "message": "Student Dropout Prediction API"}'
        }
    
    # Prediction endpoint
    if request.method == 'POST':
        try:
            import json
            
            # Parse request body
            if hasattr(request, 'body'):
                data = json.loads(request.body)
            elif hasattr(request, 'get_json'):
                data = request.get_json()
            else:
                data = {}
            
            features = data.get('features', [])
            
            # Simple rule-based prediction
            if len(features) >= 23:
                admission_grade = float(features[6]) if features[6] else 140
                sem1_grade = float(features[14]) if features[14] else 12
                sem2_grade = float(features[20]) if features[20] else 12
                
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
                'probability': round(probability, 2),
                'message': 'Graduate' if prediction == 0 else 'At Risk of Dropout',
                'note': 'Rule-based prediction system'
            }
            
            return {
                'statusCode': 200,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Content-Type': 'application/json'
                },
                'body': json.dumps(result)
            }
            
        except Exception as e:
            return {
                'statusCode': 500,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Content-Type': 'application/json'
                },
                'body': json.dumps({
                    'error': f'Prediction failed: {str(e)}',
                    'prediction': 1,
                    'probability': 0.50
                })
            }
    
    # Method not allowed
    return {
        'statusCode': 405,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json'
        },
        'body': '{"error": "Method not allowed"}'
    }


# Export the handler for Vercel
def main(request):
    return handler(request)