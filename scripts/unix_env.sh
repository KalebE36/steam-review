#!/bin/bash
# This script sets up the local development environment

echo "Creating virtual environment..."
python -m venv venv

# Note: Activating in a script is tricky and often doesn't
# affect the parent shell. This is better run as:
# source setup_env.sh
# Or just run the commands manually.
# For simplicity, we'll just install using the venv's pip.
echo "Installing packages..."

source venv/bin/activate
pip install -r requirements.txt

echo "Environment setup complete."
