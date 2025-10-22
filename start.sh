#!/bin/bash

# Crowdfunding Platform Launcher Script
# This script makes it easy to start the application

echo "🌟 Starting Crowdfunding Platform..."
echo "==============================================="

# Check if Python is installed
if ! command -v python &> /dev/null; then
    echo "❌ Python is not installed or not in PATH"
    echo "💡 Please install Python 3.7 or higher first"
    echo "   Visit: https://www.python.org/downloads/"
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "🐍 Python version: $PYTHON_VERSION"

# Check if we're in the right directory
if [ ! -f "main.py" ]; then
    echo "❌ main.py not found!"
    echo "💡 Please run this script from the crowdfunding platform directory"
    exit 1
fi

echo "✅ All checks passed!"
echo "🚀 Launching application..."
echo ""

# Run the application
python main.py

echo ""
echo "👋 Thank you for using the Crowdfunding Platform!"
echo "🌟 Have a great day!"