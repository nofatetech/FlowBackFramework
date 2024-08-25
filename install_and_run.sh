#!/bin/bash

# Set up virtual environment directory name
VENV_DIR=venv

# Check if the virtual environment already exists
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv $VENV_DIR
fi

# Activate the virtual environment
source $VENV_DIR/bin/activate

# Install dependencies from requirements.txt
echo "Installing dependencies..."
pip install -r requirements.txt

# Run the Flask app
echo "Running Flask app..."
export FLASK_APP=app.py
export FLASK_ENV=development
flask run

# Deactivate the virtual environment when done
deactivate

# Pause equivalent for Linux (optional)
read -p "Press any key to continue..."
