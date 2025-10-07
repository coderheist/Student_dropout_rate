import json

def app(environ, start_response):
    """WSGI application for Vercel"""
    
    method = environ.get('REQUEST_METHOD', 'GET')
    path = environ.get('PATH_INFO', '/')
    
    # CORS headers
    headers = [
        ('Access-Control-Allow-Origin', '*'),
        ('Access-Control-Allow-Methods', 'GET, POST, OPTIONS'),
        ('Access-Control-Allow-Headers', 'Content-Type'),
        ('Content-Type', 'application/json')
    ]
    
    # Handle OPTIONS (CORS preflight)
    if method == 'OPTIONS':
        start_response('200 OK', headers)
        return [b'']
    
    # Handle GET (health check)
    if method == 'GET':
        response = {
            'status': 'API is working',
            'message': 'Student Dropout Prediction API',
            'path': path
        }
        start_response('200 OK', headers)
        return [json.dumps(response).encode('utf-8')]
    
    # Handle POST (prediction)
    if method == 'POST':
        try:
            # Read request body
            content_length = int(environ.get('CONTENT_LENGTH', 0))
            if content_length > 0:
                request_body = environ['wsgi.input'].read(content_length)
                data = json.loads(request_body.decode('utf-8'))
            else:
                data = {}
            
            features = data.get('features', [])
            
            # Simple prediction
            prediction = 1
            probability = 0.5
            
            if len(features) > 6:
                try:
                    admission_grade = float(features[6])
                    if admission_grade > 150:
                        prediction = 0
                        probability = 0.8
                    else:
                        prediction = 1
                        probability = 0.7
                except (ValueError, IndexError):
                    pass
            
            result = {
                'prediction': prediction,
                'probability': probability,
                'message': 'Graduate' if prediction == 0 else 'At Risk of Dropout'
            }
            
            start_response('200 OK', headers)
            return [json.dumps(result).encode('utf-8')]
            
        except Exception as e:
            error_response = {
                'error': str(e),
                'prediction': 1,
                'probability': 0.5
            }
            start_response('500 Internal Server Error', headers)
            return [json.dumps(error_response).encode('utf-8')]
    
    # Method not allowed
    start_response('405 Method Not Allowed', headers)
    return [json.dumps({'error': 'Method not allowed'}).encode('utf-8')]