#!/bin/bash
# Quick Start Script - Runs both frontend and backend
# Requires Python 3.12.8

set -e

echo "☁️  Cloud RAG System - Quick Start"
echo "=================================="

# Check Python version
echo "Checking Python version..."
PYTHON_VERSION=$(python --version 2>&1 | awk '{print $2}')
REQUIRED_VERSION="3.12.8"

if [[ "$PYTHON_VERSION" != "$REQUIRED_VERSION" ]]; then
    echo "⚠️  WARNING: Python version mismatch!"
    echo "   Required: Python $REQUIRED_VERSION"
    echo "   Found:    Python $PYTHON_VERSION"
    echo ""
    read -p "Continue anyway? (y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Exiting. Please install Python $REQUIRED_VERSION"
        exit 1
    fi
else
    echo "✅ Python $PYTHON_VERSION detected"
fi

# Check for .env
if [ ! -f .env ]; then
    echo "Creating .env from template..."
    cp .env.example .env
    echo ""
    echo "⚠️  IMPORTANT: Edit .env and add your HuggingFace token!"
    echo "Get your token: https://huggingface.co/settings/tokens"
    echo ""
    read -p "Press Enter after adding your token to .env..."
fi

# Load env
export $(cat .env | xargs)

if [ -z "$HF_TOKEN" ]; then
    echo "❌ HF_TOKEN not set. Please edit .env file."
    exit 1
fi

# Setup backend
echo ""
echo "📦 Setting up backend..."
cd backend
if [ ! -d venv ]; then
    echo "Creating virtual environment with Python $PYTHON_VERSION..."
    python -m venv venv
fi
source venv/bin/activate

echo "Installing dependencies (this may take a minute)..."
pip install --upgrade pip
pip install -r requirements.txt

cd ..

# Start backend in background
echo "🚀 Starting backend on http://localhost:8000"
cd backend
source venv/bin/activate
python app.py &
BACKEND_PID=$!
cd ..

# Wait for backend to start
sleep 3

# Start frontend
echo "🌐 Starting frontend on http://localhost:3000"
echo ""
echo "✅ System ready!"
echo "   Frontend: http://localhost:3000"
echo "   Backend:  http://localhost:8000"
echo "   Diagnostics: http://localhost:3000/test.html"
echo ""
echo "Press Ctrl+C to stop all services"
cd frontend
python -m http.server 3000

# Cleanup on exit
kill $BACKEND_PID
