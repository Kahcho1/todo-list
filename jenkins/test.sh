#!/bin/bash

echo "Test Stage"

# venv created + source
python3 -m venv venv
source venv/bin/activate

# install pytest, flask_testing and requirements for frontend and backend
pip install pytest pytest-cov flask_testing
pip3 install -r frontend/requirements.txt
pip3 install -r frontend/requirements.txt

# run pytest frontend
python3 -m pytest frontend

# run pytest frontend
python3 -m pytest backend

# remove venv
deactivate
rm -rf venv

# # testing
# python3 -m pytest \
#     --cov=application \
#     --cov-report term-missing \
#     --cov-report xml:coverage.xml \
#     --junitxml=junit_report.xml
