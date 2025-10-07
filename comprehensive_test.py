"""
Comprehensive Deployment Tester
Tests multiple scenarios and provides detailed diagnostics
"""
import requests
import time
import json

def test_endpoint_detailed(url, endpoint=""):
    """Test endpoint with detailed error reporting"""
    full_url = f"{url}{endpoint}"
    print(f"Testing: {full_url}")
    
    try:
        response = requests.get(full_url, timeout=15)
        print(f"   Status: {response.status_code}")
        
        if response.status_code == 200:
            try:
                data = response.json()
                print(f"   ✅ SUCCESS! Response: {json.dumps(data, indent=2)}")
                return True, data
            except:
                print(f"   ✅ SUCCESS! (Non-JSON response)")
                return True, response.text[:200]
        elif response.status_code == 502:
            print(f"   ❌ 502 Bad Gateway - App is crashing or not starting properly")
            return False, "502_error"
        elif response.status_code == 503:
            print(f"   ❌ 503 Service Unavailable - App is starting up or overloaded")
            return False, "503_error"
        elif response.status_code == 404:
            print(f"   ❌ 404 Not Found - Endpoint doesn't exist")
            return False, "404_error"
        else:
            print(f"   ⚠️ Unexpected status: {response.status_code}")
            print(f"   Response: {response.text[:200]}")
            return False, f"status_{response.status_code}"
            
    except requests.exceptions.ConnectTimeout:
        print(f"   ❌ Connection timeout - Server not responding")
        return False, "timeout"
    except requests.exceptions.ConnectionError as e:
        if "Read timed out" in str(e):
            print(f"   ❌ Read timeout - Server is slow or overloaded")
            return False, "read_timeout"
        else:
            print(f"   ❌ Connection failed: {str(e)[:100]}")
            return False, "connection_error"
    except Exception as e:
        print(f"   ❌ Unexpected error: {str(e)[:100]}")
        return False, "unexpected_error"

def test_prediction_endpoint(base_url):
    """Test the prediction endpoint specifically"""
    print(f"\n🤖 Testing Prediction Endpoint...")
    
    # Simple test data
    test_data = {
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
            f"{base_url}/predict",
            json=test_data,
            headers={'Content-Type': 'application/json'},
            timeout=20
        )
        
        print(f"   Status: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"   ✅ Prediction Success!")
            print(f"   Result: {result.get('prediction_label', 'Unknown')}")
            print(f"   Confidence: {result.get('confidence', 'N/A')}")
            print(f"   Model: {result.get('model_used', 'Unknown')}")
            return True
        else:
            print(f"   ❌ Prediction failed")
            print(f"   Response: {response.text[:200]}")
            return False
            
    except Exception as e:
        print(f"   ❌ Prediction error: {str(e)[:100]}")
        return False

def main():
    print("🔍 Comprehensive Deployment Test")
    print("=" * 50)
    
    # Test multiple potential URLs
    test_urls = [
        "https://student-dropout-rate.onrender.com",
        "https://student-dropout.onrender.com",
        "https://studentdropout.onrender.com",
        "https://student-dropout-prediction.onrender.com",
        "https://dropout-prediction.onrender.com"
    ]
    
    working_url = None
    
    for url in test_urls:
        print(f"\n🌐 Testing: {url}")
        print("-" * 40)
        
        # Test multiple endpoints
        success_count = 0
        
        # Test root endpoint
        success, _ = test_endpoint_detailed(url, "/")
        if success:
            success_count += 1
            working_url = url
        
        # Test health endpoint
        success, _ = test_endpoint_detailed(url, "/health")
        if success:
            success_count += 1
            working_url = url
            
        # If we found a working URL, test prediction
        if success_count > 0:
            print(f"   Found working endpoints: {success_count}/2")
            if test_prediction_endpoint(url):
                success_count += 1
            break
        
        print(f"   Working endpoints: {success_count}/2")
        time.sleep(2)  # Pause between URL tests
    
    # Summary
    print(f"\n" + "=" * 50)
    if working_url:
        print(f"🎉 DEPLOYMENT FOUND: {working_url}")
        print(f"\n🔗 Test URLs:")
        print(f"   Home: {working_url}")
        print(f"   Health: {working_url}/health")
        print(f"   API Docs: {working_url}/")
        print(f"   Frontend: {working_url}/frontend-simple/")
    else:
        print(f"❌ NO WORKING DEPLOYMENT FOUND")
        print(f"\n🔍 Possible Issues:")
        print(f"   1. Deployment still building (check Render dashboard)")
        print(f"   2. Build script failed (check build logs)")
        print(f"   3. App crashing on startup (check runtime logs)")
        print(f"   4. Wrong URL pattern")
        
        print(f"\n💡 Next Steps:")
        print(f"   1. Check Render dashboard: https://dashboard.render.com")
        print(f"   2. Look for build errors in logs")
        print(f"   3. Verify Python version compatibility")
        print(f"   4. Check if simple app is being used")

if __name__ == "__main__":
    main()