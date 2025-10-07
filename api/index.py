from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

# Add backend directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))

from app import app

# This is the Vercel serverless function handler
def handler(event, context):
    return app