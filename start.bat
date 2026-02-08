@echo off
REM Quick Start Script - Runs both frontend and backend
REM Requires Python 3.12.8

echo ☁️  Cloud RAG System - Quick Start
echo ==================================

REM Check Python version
echo Checking Python version...
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
set REQUIRED_VERSION=3.12.8

if not "%PYTHON_VERSION%"=="%REQUIRED_VERSION%" (
    echo ⚠️  WARNING: Python version mismatch!
    echo    Required: Python %REQUIRED_VERSION%
    echo    Found:    Python %PYTHON_VERSION%
    echo.
    set /p CONTINUE="Continue anyway? (y/n): "
    if /i not "%CONTINUE%"=="y" (
        echo Exiting. Please install Python %REQUIRED_VERSION%
        exit /b 1
    )
) else (
    echo ✅ Python %PYTHON_VERSION% detected
)

REM Check for .env
if not exist .env (
    echo Creating .env from template...
    copy .env.example .env
    echo.
    echo ⚠️  IMPORTANT: Edit .env and add your HuggingFace token!
    echo Get your token: https://huggingface.co/settings/tokens
    echo.
    pause
)

REM Setup backend
echo.
echo 📦 Setting up backend...
cd backend
if not exist venv (
    echo Creating virtual environment with Python %PYTHON_VERSION%...
    python -m venv venv
)
call venv\Scripts\activate

echo Installing dependencies (this may take a minute)...
python -m pip install --upgrade pip
pip install -r requirements.txt

REM Start backend in background
echo 🚀 Starting backend on http://localhost:8000
start /B python app.py
cd ..

REM Wait for backend
timeout /t 3 /nobreak > nul

REM Start frontend
echo 🌐 Starting frontend on http://localhost:3000
echo.
echo ✅ System ready!
echo    Frontend: http://localhost:3000
echo    Backend:  http://localhost:8000
echo    Diagnostics: http://localhost:3000/test.html
echo.
echo Press Ctrl+C to stop all services
cd frontend
python -m http.server 3000
