@echo off
echo "Creating virtual environment..."
python -m venv venv

echo "Installing packages..."

REM This activates the virtual environment for the rest of this script
call venv\Scripts\activate.bat

REM Now that the environment is active, 'pip' will point to the venv's pip
pip install -r requirements.txt

echo "Environment setup complete."
echo "To activate this environment in your terminal, run: venv\Scripts\activate.bat"