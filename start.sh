#!/bin/bash

# Create a virtual environment named 'venv'
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install Flask and other requirements
pip install -r requirements.txt

# Run the main.py script
python main.py

# Deactivate the virtual environment
deactivate

