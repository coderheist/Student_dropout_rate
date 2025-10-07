#!/usr/bin/env bash
# Render start script

echo "Starting Student Dropout Prediction API..."
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
else
    echo "app.py not found in $(pwd)"
    ls -la
fi

echo "Starting gunicorn..."
exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --timeout 120 --log-level debug app:app