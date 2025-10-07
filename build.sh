#!/usecho "Python version check..."
python --version

echo "Upgrading pip and build tools..."n/env bash
# Render build script

set -o errexit  # Exit on any error

echo "� Python version check..."
python --version

echo "�🔧 Upgrading pip and build tools..."
pip install --upgrade pip setuptools wheel

echo "Installing Python dependencies with binary wheels..."
pip install --only-binary=all -r requirements.txt

echo "Checking ML model..."
if [ -f "random_forest_model.pkl" ]; then
    echo "ML model found: random_forest_model.pkl"
else
    echo "ML model not found, will create sample model"
fi

echo "Build complete!"