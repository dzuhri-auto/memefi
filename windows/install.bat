@echo off

:: Specify the Python version you want to install
set "PYTHON_VERSION=3.10.12"

:: Check if Python is installed and get the version
for /f "delims=" %%i in ('python --version 2^>^&1') do set "INSTALLED_VERSION=%%i"
echo Installed Python version: %INSTALLED_VERSION%

:: Compare installed version with the desired version
if "%INSTALLED_VERSION:~7%"=="%PYTHON_VERSION%" (
    echo The desired Python version %PYTHON_VERSION% is already installed.
) else (
    echo Installing Python %PYTHON_VERSION%...

    :: Download the installer (64-bit version for example)
    powershell -Command "Start-Process 'https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe' -ArgumentList '/quiet InstallAllUsers=1 PrependPath=1' -Wait"

    :: Verify the installation
    python --version
    if "%ERRORLEVEL%"=="0" (
        echo Python %PYTHON_VERSION% has been successfully installed.
    ) else (
        echo Failed to install Python %PYTHON_VERSION%.
    )
)

:: Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

if not exist "venv\installed" (
    if exist "requirements.txt" (
        echo Installing wheel for faster installing
        pip install wheel
        echo Installing dependencies...
        pip install -r requirements.txt
        echo. > venv\installed
    ) else (
        echo requirements.txt not found, skipping dependency installation.
    )
) else (
    echo Dependencies already installed, skipping installation.
)

if not exist ".env" (
    echo Copying configuration file
    copy .env-example .env
) else (
    echo Skipping .env copying
)

echo Done..
echo PLEASE EDIT .ENV FILE
pause
