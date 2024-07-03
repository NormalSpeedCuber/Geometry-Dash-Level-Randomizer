#!/bin/bash

if ! python3 --version | grep -q "Python 3.11.4"; then
    echo "Installing Python 3.11.4..."

    brew install python@3.11

else
    echo "Python 3.11.4 is already installed."
fi


pip install flask
pip install random

echo "Installation complete."
