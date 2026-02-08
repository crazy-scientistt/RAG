@echo off
REM Backend startup script for Windows
REM Requires Python 3.12.8

echo 🚀 Starting Cloud RAG Backend...

REM Check Python version
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
set REQUIRED_VERSION=3.12.8

if not "%PYTHON_VERSION%"=="%REQUIRED_VERSION%" (
    echo ⚠️  WARNING: Python version mismatch!
    echo    Required: Python %REQUIRED_VERSION%
    echo    Found:    Python %PYTHON_VERSION%
    echo.
)

REM Check if .env exists
if not exist ..\.env (
    echo ⚠️  No .env file found. Creating from .env.example...
    copy ..\.env.example ..\.env
    echo ❗ Please edit .env and add your HuggingFace token
    exit /b 1
)

REM Install dependencies if needed
if not exist venv (
    echo 📦 Creating virtual environment...
    python -m venv venv
    call venv\Scripts\activate
    echo 📦 Installing dependencies...
    python -m pip install --upgrade pip
    pip install -r requirements.txt
) else (
    call venv\Scripts\activate
)

echo ✅ Starting server on http://localhost:8000
python app.py
