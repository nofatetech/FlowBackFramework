@echo off

REM Set up virtual environment directory name
set VENV_DIR=venv

REM Check if the virtual environment already exists
if not exist %VENV_DIR% (
    echo Creating virtual environment...
    python -m venv %VENV_DIR%
)

REM Activate the virtual environment
call %VENV_DIR%\Scripts\activate

REM Install dependencies from requirements.txt
echo Installing dependencies...
pip install -r requirements.txt

REM Run the Flask app
echo Running Flask app...
set FLASK_APP=app.py
set FLASK_ENV=development
flask run

REM Deactivate the virtual environment when done
deactivate

pause
