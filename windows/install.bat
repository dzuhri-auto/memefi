@echo off

:: Specify the Python version you want to install
set PYTHON_VERSION=3.10.14

:: Check if Python is installed and get the version
for /f "tokens=2 delims==" %%i in ('python --version 2^>^&1') do (
    set INSTALLED_VERSION=%%i
)

echo Installed Python version: %INSTALLED_VERSION%

:: Compare installed version with the desired version
if "%INSTALLED_VERSION%"=="%PYTHON_VERSION%" (
    echo The desired Python version %PYTHON_VERSION% is already installed.
) else (
    echo Installing Python %PYTHON_VERSION%...

    :: Download the Python installer
    powershell -Command "Invoke-WebRequest -Uri https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe -OutFile python-%PYTHON_VERSION%-amd64.exe"

    :: Install Python silently
    python-%PYTHON_VERSION%-amd64.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

    :: Verify the installation
    python --version
    if "%ERRORLEVEL%"=="0" (
        echo Python %PYTHON_VERSION% has been successfully installed.
    ) else (
        echo Failed to install Python %PYTHON_VERSION%.
        exit /b 1
    )
)

:: Create virtual environment if it doesn't exist
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

:: Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

:: Install dependencies if they haven't been installed yet
if not exist venv\installed (
    if exist requirements.txt (
        echo Installing wheel for faster installations...
        pip install wheel
        echo Installing dependencies...
        pip install -r requirements.txt
        echo.>venv\installed
    ) else (
        echo requirements.txt not found, skipping dependency installation.
    )
) else (
    echo Dependencies already installed, skipping installation.
)

:: Copy .env-example to .env if .env doesn't exist
if not exist .env (
    echo Copying configuration file...
    copy .env-example .env
) else (
    echo Skipping .env copying...
)

echo Done.
echo PLEASE EDIT .ENV FILE
