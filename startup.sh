#!/bin/bash
# Azure App Service Startup Script for Python Flask Application

echo "Starting Azure App Service - Clinic Management API"

# Set environment variables
export PYTHONUNBUFFERED=1

# Ensure we're in the correct directory
cd /home/site/wwwroot

# Check if virtual environment exists, if not create it
if [ ! -d "antenv" ]; then
    echo "Creating virtual environment..."
    python -m venv antenv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source antenv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
python -m pip install --upgrade pip

# Install/update dependencies
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

# Initialize database if it doesn't exist
if [ ! -f "/home/clinic.db" ]; then
    echo "Initializing database..."
    python -c "from app import app, db; app.app_context().push(); db.create_all(); print('Database initialized')"
fi

# Start Gunicorn
echo "Starting Gunicorn server..."
gunicorn --bind=0.0.0.0:8000 --timeout 600 --workers 4 --access-logfile '-' --error-logfile '-' app:app
