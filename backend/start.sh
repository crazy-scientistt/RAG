#!/bin/bash

echo "===================================="
echo "  Cloud RAG Backend - Starting"
echo "===================================="
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install requirements
echo "Installing dependencies..."
pip install -r requirements.txt

# Check for HF_TOKEN
if [ -z "$HF_TOKEN" ]; then
    echo ""
    echo "WARNING: HF_TOKEN environment variable not set!"
    echo "Please set it with: export HF_TOKEN=your_token_here"
    echo ""
    read -p "Press enter to continue..."
fi

# Start the server
echo ""
echo "Starting backend server on http://localhost:8000"
echo ""
python app.py
