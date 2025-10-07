"""Test script for ML model integration"""
from app import app, model, FEATURE_ORDER

print("=" * 60)
print("MODEL STATUS CHECK")
print("=" * 60)
print(f"Model loaded: {model is not None}")
print(f"Number of features expected: {len(FEATURE_ORDER)}")
print(f"\nFeature order:")
for i, feat in enumerate(FEATURE_ORDER, 1):
    print(f"{i:2d}. {feat}")

# Test prediction with sample data
print("\n" + "=" * 60)
print("TESTING PREDICTION WITH ALL 23 PARAMETERS")
print("=" * 60)

sample_data = {
    'marital_status': 1,
    'application_mode': 1,
    'course': 9238,
    'daytime_evening_attendance': 1,
    'previous_qualification': 1,
    'nationality': 1,
    'mothers_qualification': 13,
    'fathers_qualification': 10,
    'mothers_occupation': 6,
    'fathers_occupation': 10,
    'displaced': 0,
    'educational_special_needs': 0,
    'debtor': 0,
    'tuition_fees_up_to_date': 1,
    'gender': 1,
    'scholarship_holder': 0,
    'age_at_enrollment': 20,
    'international': 0,
    'curricular_units_1st_sem_credited': 6,
    'curricular_units_1st_sem_grade': 14.5,
    'curricular_units_2nd_sem_credited': 6,
    'curricular_units_2nd_sem_grade': 13.8,
    'curricular_units_1st_sem_approved': 6
}

# Test via API
client = app.test_client()
response = client.post('/predict', json=sample_data)
result = response.get_json()

print(f"\nPrediction: {result.get('prediction')}")
print(f"Label: {result.get('prediction_label')}")
print(f"Confidence: {result.get('confidence')}")
print(f"Model used: {result.get('model_used')}")
print(f"Parameters used: {result.get('parameters_used', 'N/A')}")

# Test health endpoint
print("\n" + "=" * 60)
print("HEALTH CHECK")
print("=" * 60)
health_response = client.get('/health')
health = health_response.get_json()
print(f"Status: {health.get('status')}")
print(f"Model: {health.get('model')}")
print(f"Parameters: {health.get('parameters')}")

print("\n✅ All tests completed!")
