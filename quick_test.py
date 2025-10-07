"""
Quick Manual Test - Replace YOUR_RENDER_URL with your actual URL
"""
import requests
import json

# Replace this with your actual Render URL
BASE_URL = "https://your-app-name.onrender.com"  # CHANGE THIS!

def test_quick():
    print(f"Testing API at: {BASE_URL}")
    
    # Test 1: Health check
    print("\n1. Health Check...")
    try:
        response = requests.get(f"{BASE_URL}/health", timeout=10)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Test 2: Prediction
    print("\n2. Sample Prediction...")
    sample_data = {
        "marital_status": 1,
        "application_mode": 1,
        "course": 9238,
        "daytime_evening_attendance": 1,
        "previous_qualification": 1,
        "nationality": 1,
        "mothers_qualification": 1,
        "fathers_qualification": 1,
        "mothers_occupation": 1,
        "fathers_occupation": 1,
        "displaced": 0,
        "educational_special_needs": 0,
        "debtor": 0,
        "tuition_fees_up_to_date": 1,
        "gender": 1,
        "scholarship_holder": 1,
        "age_at_enrollment": 20,
        "international": 0,
        "curricular_units_1st_sem_credited": 5,
        "curricular_units_1st_sem_grade": 15.5,
        "curricular_units_2nd_sem_credited": 5,
        "curricular_units_2nd_sem_grade": 16.0,
        "curricular_units_1st_sem_approved": 5
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/predict", 
            json=sample_data,
            headers={'Content-Type': 'application/json'},
            timeout=15
        )
        print(f"Status: {response.status_code}")
        result = response.json()
        print(f"Prediction: {result.get('prediction_label')}")
        print(f"Confidence: {result.get('confidence')}")
        print(f"Model: {result.get('model_used')}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("🚨 IMPORTANT: Edit this file and replace BASE_URL with your Render URL!")
    print(f"Current URL: {BASE_URL}")
    if "your-app-name" in BASE_URL:
        print("❌ You need to update the BASE_URL first!")
    else:
        test_quick()