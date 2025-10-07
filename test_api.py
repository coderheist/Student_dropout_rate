#!/usr/bin/env python3
"""
Student Dropout Prediction API Tester
Tests all endpoints and prediction scenarios
"""

import requests
import json
import time

# Test data samples
test_cases = [
    {
        "name": "High Risk Student",
        "data": {
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
            "debtor": 1,  # High risk: is a debtor
            "tuition_fees_up_to_date": 0,  # High risk: tuition not up to date
            "gender": 1,
            "scholarship_holder": 0,
            "age_at_enrollment": 35,  # High risk: older student
            "international": 0,
            "curricular_units_1st_sem_credited": 2,  # Low credits
            "curricular_units_1st_sem_grade": 8.5,  # Poor grades
            "curricular_units_2nd_sem_credited": 1,  # Very low credits
            "curricular_units_2nd_sem_grade": 7.2,  # Poor grades
            "curricular_units_1st_sem_approved": 1
        },
        "expected": "Dropout"
    },
    {
        "name": "Low Risk Student",
        "data": {
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
            "debtor": 0,  # Low risk: not a debtor
            "tuition_fees_up_to_date": 1,  # Low risk: tuition up to date
            "gender": 1,
            "scholarship_holder": 1,  # Low risk: has scholarship
            "age_at_enrollment": 19,  # Low risk: normal age
            "international": 0,
            "curricular_units_1st_sem_credited": 6,  # Good credits
            "curricular_units_1st_sem_grade": 16.8,  # Excellent grades
            "curricular_units_2nd_sem_credited": 6,  # Good credits
            "curricular_units_2nd_sem_grade": 17.2,  # Excellent grades
            "curricular_units_1st_sem_approved": 6
        },
        "expected": "Graduate"
    },
    {
        "name": "Medium Risk Student",
        "data": {
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
            "scholarship_holder": 0,
            "age_at_enrollment": 22,  # Slightly older
            "international": 0,
            "curricular_units_1st_sem_credited": 4,  # Average credits
            "curricular_units_1st_sem_grade": 12.5,  # Average grades
            "curricular_units_2nd_sem_credited": 5,  # Average credits
            "curricular_units_2nd_sem_grade": 13.1,  # Average grades
            "curricular_units_1st_sem_approved": 4
        },
        "expected": "Enrolled"
    }
]

def test_api(base_url):
    """Test the Student Dropout Prediction API"""
    print("🧪 Testing Student Dropout Prediction API")
    print(f"🌐 Base URL: {base_url}")
    print("=" * 60)
    
    # Test 1: Health Check
    print("\n1️⃣ Testing Health Endpoint...")
    try:
        response = requests.get(f"{base_url}/health", timeout=10)
        if response.status_code == 200:
            print("✅ Health check passed!")
            print(f"   Response: {response.json()}")
        else:
            print(f"❌ Health check failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Health check error: {e}")
    
    # Test 2: Home Page
    print("\n2️⃣ Testing Home Endpoint...")
    try:
        response = requests.get(f"{base_url}/", timeout=10)
        if response.status_code == 200:
            print("✅ Home page accessible!")
            home_data = response.json()
            print(f"   API Version: {home_data.get('version', 'Unknown')}")
            print(f"   Model: {home_data.get('model', 'Unknown')}")
        else:
            print(f"❌ Home page failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Home page error: {e}")
    
    # Test 3: Prediction Endpoint
    print("\n3️⃣ Testing Prediction Endpoint...")
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n   Test Case {i}: {test_case['name']}")
        print(f"   Expected: {test_case['expected']}")
        
        try:
            response = requests.post(
                f"{base_url}/predict",
                json=test_case['data'],
                headers={'Content-Type': 'application/json'},
                timeout=15
            )
            
            if response.status_code == 200:
                result = response.json()
                prediction_label = result.get('prediction_label', 'Unknown')
                confidence = result.get('confidence', 0)
                model_used = result.get('model_used', 'unknown')
                
                print(f"   ✅ Prediction: {prediction_label}")
                print(f"   📊 Confidence: {confidence:.3f}")
                print(f"   🤖 Model: {model_used}")
                
                # Check if prediction makes sense
                if prediction_label in ['Dropout', 'Enrolled', 'Graduate']:
                    print("   ✅ Valid prediction category")
                else:
                    print("   ⚠️ Unexpected prediction category")
                    
            else:
                print(f"   ❌ Prediction failed: {response.status_code}")
                print(f"   Response: {response.text}")
                
        except Exception as e:
            print(f"   ❌ Prediction error: {e}")
        
        time.sleep(1)  # Small delay between requests
    
    # Test 4: Error Handling
    print("\n4️⃣ Testing Error Handling...")
    try:
        response = requests.post(
            f"{base_url}/predict",
            json={},  # Empty data
            headers={'Content-Type': 'application/json'},
            timeout=10
        )
        
        if response.status_code in [200, 400]:
            result = response.json()
            if 'error' in result or 'prediction' in result:
                print("✅ Error handling works correctly")
                print(f"   Response: {result}")
            else:
                print("⚠️ Unexpected error response format")
        else:
            print(f"⚠️ Unexpected status code: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error handling test failed: {e}")
    
    print("\n" + "=" * 60)
    print("🎯 Testing Complete!")
    print("\n💡 Next Steps:")
    print("   1. Check that predictions make logical sense")
    print("   2. Test the web interface at the base URL")
    print("   3. Try different input combinations")

if __name__ == "__main__":
    print("🔍 Student Dropout Prediction API Tester")
    print("\n📝 Please provide your Render app URL:")
    print("   Example: https://your-app-name.onrender.com")
    
    base_url = input("\n🌐 Enter your app URL: ").strip()
    
    if not base_url.startswith('http'):
        base_url = 'https://' + base_url
    
    if base_url.endswith('/'):
        base_url = base_url[:-1]
    
    test_api(base_url)