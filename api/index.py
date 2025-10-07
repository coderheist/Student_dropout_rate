"""
Simple Python serverless function for Vercel
Zero dependencies, basic prediction logic
"""

def handler(event, context):
    import json
    
    # Get HTTP method and path
    method = event.get('httpMethod', 'GET')
    
    # CORS headers
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Content-Type': 'application/json'
    }
    
    # Handle CORS preflight
    if method == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': headers,
            'body': ''
        }
    
    # Handle GET (health check)
    if method == 'GET':
        response = {
            'status': 'working',
            'message': 'Student Dropout Prediction API',
            'version': '1.0'
        }
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps(response)
        }
    
    # Handle POST (prediction)
    if method == 'POST':
        try:
            # Parse request body
            body = event.get('body', '{}')
            if isinstance(body, str):
                data = json.loads(body)
            else:
                data = body or {}
            
            features = data.get('features', [])
            
            # Simple prediction
            prediction = 1  # Default: at risk
            probability = 0.5
            
            if len(features) > 6:
                try:
                    grade = float(features[6])
                    if grade > 150:
                        prediction = 0
                        probability = 0.8
                    else:
                        prediction = 1
                        probability = 0.7
                except:
                    pass
            
            result = {
                'prediction': prediction,
                'probability': probability,
                'message': 'Graduate' if prediction == 0 else 'At Risk'
            }
            
            return {
                'statusCode': 200,
                'headers': headers,
                'body': json.dumps(result)
            }
            
        except Exception as e:
            return {
                'statusCode': 500,
                'headers': headers,
                'body': json.dumps({
                    'error': str(e),
                    'prediction': 1,
                    'probability': 0.5
                })
            }
    
    # Method not allowed
    return {
        'statusCode': 405,
        'headers': headers,
        'body': json.dumps({'error': 'Method not allowed'})
    }