#!/bin/bash

# Specify the Python version you want to install
PYTHON_VERSION="3.10.12"

# Check if Python is installed and get the version
if command -v python3 &>/dev/null; then
    INSTALLED_VERSION=$(python3 --version | awk '{print $2}')
    echo "Installed Python version: $INSTALLED_VERSION"
else
    echo "Python is not installed."
    INSTALLED_VERSION=""
fi

# Compare installed version with the desired version
if [[ "$INSTALLED_VERSION" == "$PYTHON_VERSION" ]]; then
    echo "The desired Python version $PYTHON_VERSION is already installed."
else
    echo "Installing Python $PYTHON_VERSION..."

    # Install dependencies
    sudo apt-get update
    sudo apt install software-properties-common -y

    # Add custom apt repository
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt-get update

    # Install python 3.10
    sudo apt install python3.10 python3.10-venv python3.10-dev

    # Make symbolic link
    ls -la /usr/bin/python3
    sudo rm /usr/bin/python3
    sudo ln -s python3.10 /usr/bin/python3

    # Verify the installation
    if python3.10 --version &>/dev/null; then
        echo "Python $PYTHON_VERSION has been successfully installed."
    else
        echo "Failed to install Python $PYTHON_VERSION."
    fi
fi


if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

if [ ! -f "venv/installed" ]; then
    if [ -f "requirements.txt" ]; then
		echo "Installing wheel for faster installing"
		pip3 install wheel
        echo "Installing dependencies..."
        pip3 install -r requirements.txt
        touch venv/installed
    else
        echo "requirements.txt not found, skipping dependency installation."
    fi
else
    echo "Dependencies already installed, skipping installation."
fi

if [ ! -f ".env" ]; then
	echo "Copying configuration file"
	cp .env-example .env
else
	echo "Skipping .env copying"
fi

echo "Done.."
echo "PLEASE EDIT .ENV FILE"
