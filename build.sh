#!/usr/bin/env bash
# Simple build script for Render

echo "Python version:"
python --version

echo "Installing Flask and CORS..."
pip install --upgrade pip
pip install Flask==2.3.3 Flask-CORS==4.0.0

echo "Build complete!"
ls -la