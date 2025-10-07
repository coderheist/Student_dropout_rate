from http.server import BaseHTTPRequestHandler
import json

class Handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        response = {
            "status": "API is working", 
            "message": "Student Dropout Prediction API",
            "version": "vercel-serverless"
        }
        self.wfile.write(json.dumps(response).encode('utf-8'))

    def do_POST(self):
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            if content_length > 0:
                post_data = self.rfile.read(content_length)
                data = json.loads(post_data.decode('utf-8'))
            else:
                data = {}
            
            features = data.get('features', [])
            
            # Simple prediction logic
            prediction = 1  # Default: at risk
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
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(result).encode('utf-8'))
            
        except Exception as e:
            error_response = {
                'error': str(e),
                'prediction': 1,
                'probability': 0.5
            }
            
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')  
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(error_response).encode('utf-8'))