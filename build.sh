#!/usr/bin/env bash
# Render build script - Use simple app to avoid Python 3.13 issues

set -o errexit  # Exit on any error

echo "Python version check..."
python --version

echo "Switching to simple app (no ML dependencies)..."
echo "Using simple requirements..."
pip install --upgrade pip
pip install -r requirements_simple.txt

echo "Checking if we should use simple app..."
if [ -f "app_simple.py" ]; then
    echo "Found app_simple.py - copying to backend/"
    mkdir -p backend
    cp app_simple.py backend/app.py
    echo "Using simple rule-based prediction app"
else
    echo "Using original backend app"
fi

echo "Build complete - simple version ready!"