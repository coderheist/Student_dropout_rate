#!/usr/bin/env bash
# Simple build script for Render

echo "Python version:"
python --version

echo "Installing dependencies..."
pip install --upgrade pip
pip install Flask==2.3.3 Flask-CORS==4.0.0 gunicorn==20.1.0

echo "Build complete!"
ls -la