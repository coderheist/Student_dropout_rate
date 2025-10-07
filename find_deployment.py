"""
Find and Test Render Deployment URLs
This script tests common Render URL patterns for your app
"""
import requests
import time

# Common Render URL patterns for your app
potential_urls = [
    "https://student-dropout-rate.onrender.com",
    "https://student-dropout.onrender.com", 
    "https://studentdropout.onrender.com",
    "https://student-dropout-prediction.onrender.com",
    "https://dropout-prediction.onrender.com",
    "https://coderheist-student-dropout.onrender.com"
]

def test_url(url):
    """Test if URL is accessible"""
    try:
        print(f"Testing: {url}")
        response = requests.get(f"{url}/health", timeout=10)
        if response.status_code == 200:
            print(f"✅ FOUND WORKING DEPLOYMENT: {url}")
            print(f"   Health check response: {response.json()}")
            return url
        elif response.status_code == 404:
            print(f"   ❌ 404 - App not found")
        else:
            print(f"   ⚠️ Status {response.status_code}")
    except requests.exceptions.ConnectTimeout:
        print(f"   ❌ Connection timeout")
    except requests.exceptions.ConnectionError:
        print(f"   ❌ Connection failed")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    return None

def main():
    print("🔍 Searching for your Render deployment...")
    print("=" * 50)
    
    working_url = None
    for url in potential_urls:
        working_url = test_url(url)
        if working_url:
            break
        time.sleep(1)  # Small delay between tests
    
    if working_url:
        print(f"\n🎉 SUCCESS! Your app is deployed at: {working_url}")
        print(f"\n🧪 Test your app:")
        print(f"   Health: {working_url}/health")
        print(f"   Home: {working_url}/")
        print(f"   Frontend: {working_url}/frontend-simple/")
        
        # Quick prediction test
        print(f"\n🤖 Testing prediction endpoint...")
        test_data = {
            "marital_status": 1, "application_mode": 1, "course": 9238,
            "daytime_evening_attendance": 1, "previous_qualification": 1,
            "nationality": 1, "mothers_qualification": 1, "fathers_qualification": 1,
            "mothers_occupation": 1, "fathers_occupation": 1, "displaced": 0,
            "educational_special_needs": 0, "debtor": 0, "tuition_fees_up_to_date": 1,
            "gender": 1, "scholarship_holder": 1, "age_at_enrollment": 20,
            "international": 0, "curricular_units_1st_sem_credited": 5,
            "curricular_units_1st_sem_grade": 15.5, "curricular_units_2nd_sem_credited": 5,
            "curricular_units_2nd_sem_grade": 16.0, "curricular_units_1st_sem_approved": 5
        }
        
        try:
            response = requests.post(
                f"{working_url}/predict",
                json=test_data,
                headers={'Content-Type': 'application/json'},
                timeout=15
            )
            if response.status_code == 200:
                result = response.json()
                print(f"   ✅ Prediction works!")
                print(f"   Result: {result.get('prediction_label')} (confidence: {result.get('confidence')})")
                print(f"   Model: {result.get('model_used')}")
            else:
                print(f"   ⚠️ Prediction endpoint status: {response.status_code}")
        except Exception as e:
            print(f"   ❌ Prediction test failed: {e}")
            
    else:
        print(f"\n❌ Could not find a working deployment.")
        print(f"\n💡 Check your Render dashboard:")
        print(f"   1. Go to https://dashboard.render.com")
        print(f"   2. Find your Student Dropout service")
        print(f"   3. Check if it's running and note the URL")
        print(f"   4. Look for any build errors in the logs")

if __name__ == "__main__":
    main()