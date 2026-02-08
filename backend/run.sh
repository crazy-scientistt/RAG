#!/bin/bash
# Backend startup script
# Requires Python 3.12.8

echo "🚀 Starting Cloud RAG Backend..."

# Check Python version
PYTHON_VERSION=$(python --version 2>&1 | awk '{print $2}')
REQUIRED_VERSION="3.12.8"

if [[ "$PYTHON_VERSION" != "$REQUIRED_VERSION" ]]; then
    echo "⚠️  WARNING: Python version mismatch!"
    echo "   Required: Python $REQUIRED_VERSION"
    echo "   Found:    Python $PYTHON_VERSION"
    echo ""
fi

# Check if .env exists
if [ ! -f ../.env ]; then
    echo "⚠️  No .env file found. Creating from .env.example..."
    cp ../.env.example ../.env
    echo "❗ Please edit .env and add your HuggingFace token"
    exit 1
fi

# Load environment variables
export $(cat ../.env | xargs)

# Check if HF_TOKEN is set
if [ -z "$HF_TOKEN" ]; then
    echo "❌ HF_TOKEN not set in .env file"
    echo "Please get your token from https://huggingface.co/settings/tokens"
    exit 1
fi

# Install dependencies if needed
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python -m venv venv
    source venv/bin/activate
    echo "📦 Installing dependencies..."
    pip install --upgrade pip
    pip install -r requirements.txt
else
    source venv/bin/activate
fi

echo "✅ Starting server on http://localhost:8000"
python app.py
