from http.server import BaseHTTPRequestHandler
import json
import urllib.parse

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        response = {
            "status": "API is running", 
            "message": "Student Dropout Prediction API - Zero Dependencies"
        }
        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            features = data.get('features', [])
            
            # Simple rule-based prediction
            if len(features) >= 23:
                try:
                    admission_grade = float(features[6]) if features[6] else 140
                    sem1_grade = float(features[14]) if features[14] else 12
                    sem2_grade = float(features[20]) if features[20] else 12
                except (ValueError, IndexError):
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
                'note': 'Rule-based prediction (zero dependencies)'
            }
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(result).encode())
            
        except Exception as e:
            error_response = {
                'error': f'Prediction failed: {str(e)}',
                'prediction': 1,
                'probability': 0.50,
                'message': 'At Risk of Dropout'
            }
            
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(error_response).encode())

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()