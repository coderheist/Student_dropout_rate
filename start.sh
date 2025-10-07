#!/usr/bin/env bash
# Simple start script for Render

echo "Starting app on port $PORT"
echo "Current directory: $(pwd)"
echo "Files in directory:"
ls -la

echo "Starting with gunicorn..."
exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --timeout 30 app:app