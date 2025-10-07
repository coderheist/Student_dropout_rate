#!/usr/bin/env bash
# Render build script

set -o errexit  # Exit on any error

echo "🔧 Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "🤖 Checking ML model..."
if [ -f "random_forest_model.pkl" ]; then
    echo "✅ ML model found: random_forest_model.pkl"
else
    echo "⚠️ ML model not found, will create sample model"
fi

echo "🚀 Build complete!"