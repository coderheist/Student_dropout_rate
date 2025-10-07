"""
Monitor Deployment Status - Run this in 5 minutes
"""
import requests
import time

def quick_test():
    url = "https://student-dropout-rate.onrender.com"
    
    print("🔄 Testing deployment after fixes...")
    print(f"URL: {url}")
    
    # Test health endpoint
    try:
        response = requests.get(f"{url}/health", timeout=10)
        print(f"Health Status: {response.status_code}")
        if response.status_code == 200:
            print(f"✅ DEPLOYMENT WORKING!")
            print(f"Response: {response.json()}")
            
            # Test prediction
            test_data = {"age_at_enrollment": 22, "curricular_units_1st_sem_grade": 15}
            pred_response = requests.post(f"{url}/predict", json=test_data, timeout=10)
            print(f"Prediction Status: {pred_response.status_code}")
            if pred_response.status_code == 200:
                print(f"✅ PREDICTION WORKING!")
                print(f"Result: {pred_response.json()}")
            
        elif response.status_code == 502:
            print("❌ Still getting 502 - app may still be building")
        elif response.status_code == 503:
            print("❌ 503 - service starting up, try again in 2 minutes")
        else:
            print(f"⚠️ Unexpected status: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Connection error: {e}")
        print("App may still be deploying...")

if __name__ == "__main__":
    quick_test()