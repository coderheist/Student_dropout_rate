#!/usr/bin/env bash
# Render start script

echo "🚀 Starting Student Dropout Prediction API..."
cd backend
exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --timeout 120 app:app