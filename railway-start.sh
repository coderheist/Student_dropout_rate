#!/bin/bash
# Railway deployment script

# Install Python dependencies
pip install -r backend/requirements.txt

# Start the Flask application
#!/bin/bash
echo "🚂 Starting Student Dropout Rate Application on Railway..."
echo "📦 Installing dependencies..."
pip install -r requirements.txt
echo "🔧 Loading ML model from pickle file..."
cd backend
echo "🚀 Starting Flask server..."
python app.py