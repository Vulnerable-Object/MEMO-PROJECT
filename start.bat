@echo off
REM Crowdfunding Platform Launcher Script for Windows
REM This script makes it easy to start the application

echo 🌟 Starting Crowdfunding Platform...
echo ===============================================

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo 💡 Please install Python 3.7 or higher first
    echo    Visit: https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Show Python version
for /f "tokens=2" %%i in ('python --version') do set PYTHON_VERSION=%%i
echo 🐍 Python version: %PYTHON_VERSION%

REM Check if we're in the right directory
if not exist "main.py" (
    echo ❌ main.py not found!
    echo 💡 Please run this script from the crowdfunding platform directory
    pause
    exit /b 1
)

echo ✅ All checks passed!
echo 🚀 Launching application...
echo.

REM Run the application
python main.py

echo.
echo 👋 Thank you for using the Crowdfunding Platform!
echo 🌟 Have a great day!
pause