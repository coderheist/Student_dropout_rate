import json

def handler(request, context=None):
    """Simple Vercel handler for student dropout prediction"""
    
    # CORS headers
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Content-Type': 'application/json'
    }
    
    method = getattr(request, 'method', 'GET')
    
    if method == 'OPTIONS':
        return {'statusCode': 200, 'headers': headers, 'body': ''}
    
    if method == 'GET':
        return {
            'statusCode': 200, 
            'headers': headers, 
            'body': json.dumps({"status": "API Working", "message": "Student Dropout Prediction"})
        }
    
    if method == 'POST':
        try:
            # Get request body
            body = getattr(request, 'body', '{}')
            if isinstance(body, bytes):
                body = body.decode('utf-8')
            
            data = json.loads(body) if body else {}
            features = data.get('features', [])
            
            # Simple prediction
            if len(features) >= 6:
                grade = float(features[6]) if len(features) > 6 and features[6] else 140
                prediction = 0 if grade > 150 else 1
                probability = 0.8 if grade > 150 else 0.7
            else:
                prediction = 1
                probability = 0.5
            
            result = {
                'prediction': prediction,
                'probability': probability,
                'message': 'Graduate' if prediction == 0 else 'At Risk'
            }
            
            return {'statusCode': 200, 'headers': headers, 'body': json.dumps(result)}
            
        except Exception as e:
            return {
                'statusCode': 500, 
                'headers': headers, 
                'body': json.dumps({'error': str(e), 'prediction': 1, 'probability': 0.5})
            }
    
    return {'statusCode': 405, 'headers': headers, 'body': json.dumps({'error': 'Method not allowed'})}