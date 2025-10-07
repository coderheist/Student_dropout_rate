"""Check pickle file integrity"""
import os

pkl_file = 'random_forest_model.pkl'

# Check file existence and size
if os.path.exists(pkl_file):
    size = os.path.getsize(pkl_file)
    print(f"Pickle file size: {size:,} bytes")
    
    # Check first bytes
    with open(pkl_file, 'rb') as f:
        first_bytes = f.read(50)
        print(f"First bytes: {first_bytes[:50]}")
        print(f"Hex: {first_bytes[:20].hex()}")
else:
    print(f"File {pkl_file} not found!")
