#!/usr/bin/env bash
# Render start script - Simple version

echo "Starting Student Dropout Prediction API (Simple Version)..."
echo "PORT: $PORT"
echo "Current directory: $(pwd)"

# Check if backend directory exists
if [ -d "backend" ]; then
    echo "Found backend directory"
    cd backend
    echo "Changed to backend directory: $(pwd)"
else
    echo "Backend directory not found, staying in root"
fi

# Check if app.py exists
if [ -f "app.py" ]; then
    echo "Found app.py"
    echo "App type: Simple rule-based prediction (no ML dependencies)"
else
    echo "app.py not found in $(pwd)"
    ls -la
fi

echo "Starting gunicorn with simple Flask app..."
exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --timeout 60 --log-level debug app:app