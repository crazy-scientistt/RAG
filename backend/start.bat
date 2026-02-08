@echo off
echo ====================================
echo   Cloud RAG Backend - Starting
echo ====================================
echo.

REM Check if virtual environment exists
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install requirements
echo Installing dependencies...
pip install -r requirements.txt

REM Check for HF_TOKEN
if "%HF_TOKEN%"=="" (
    echo.
    echo WARNING: HF_TOKEN environment variable not set!
    echo Please set it with: set HF_TOKEN=your_token_here
    echo.
    pause
)

REM Start the server
echo.
echo Starting backend server on http://localhost:8000
echo.
python app.py
