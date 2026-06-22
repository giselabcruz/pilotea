#!/bin/bash

# Create a virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -e .

echo "------------------------------------------------"
echo "Setup complete!"
echo "To run the Web UI, use:"
echo "source venv/bin/activate && python src/pilotea/api.py"
echo "------------------------------------------------"
