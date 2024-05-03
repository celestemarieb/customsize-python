#!/bin/bash

# confirm python is installed
if ! [[ -x "$(command -v python)" ]]
then
  echo 'Error: 
    This program runs on Python, but it looks like Python is not installed.
    To install Python, check out https://installpython3.com/' >&2
  exit 1
fi

# confirm virtual environment exists 
if [ ! -d "venv" ]; then
    echo "Error: Virtual environment could not be found. Please set up the virtual environment by typing 'python3 -m venv venv' and try again."
    exit 1
fi

# activate virtual environment
source venv/bin/activate

# Install packages from requirements.txt
pip install -r requirements.txt

# run application
python3 main.py

# deactivate virtual environment
deactivate
