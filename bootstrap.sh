#!/bin/sh
export FLASK_APP=./cashman/index.py
source $(pipenv --venv)/bin/activate
pip install python-louvain
pip3 install requests
pip3 install pyrebase
pip3 install community
pip3 install numpy
pip3 install networkx

flask run -h 0.0.0.0
