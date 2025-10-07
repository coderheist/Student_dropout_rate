#!/bin/bash
# Railway deployment script

# Install Python dependencies
pip install -r backend/requirements.txt

# Start the Flask application
cd backend && python app.py