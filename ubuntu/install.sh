#!/bin/bash

# Specify the Python version you want to install
PYTHON_VERSION="3.10.14"

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
    sudo apt-get install -y build-essential libssl-dev zlib1g-dev \
    libncurses5-dev libsqlite3-dev libreadline-dev libbz2-dev \
    libffi-dev liblzma-dev libgdbm-dev libnss3-dev libgdbm-compat-dev \
    libsqlite3-dev wget

    # Download and extract Python source
    cd /tmp
    wget https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tgz
    tar -xf Python-$PYTHON_VERSION.tgz
    cd Python-$PYTHON_VERSION

    # Configure and install
    ./configure --enable-optimizations
    make -j $(nproc)
    sudo make altinstall

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
