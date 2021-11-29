#!/bin/bash

echo "Test Stage"

# venv created + source
python3 -m venv venv
source venv/bin/activate

# install pytest, flask_testing and requirements for frontend and backend
pip install pytest pytest-cov flask_testing
pip3 install -r frontend/requirements.txt
pip3 install -r backend/requirements.txt

mkdir test_reports

# run pytest frontend
python3 -m pytest frontend \
    --cov=frontend/application \
    --cov-report term-missing \
    --cov-report xml:test_reports/frontend_coverage.xml \
    --junitxml=test_reports/frontend_junit_report.xml

# run pytest backend
python3 -m pytest backend \
    --cov=backend/application \
    --cov-report term-missing \
    --cov-report xml:test_reports/backend_coverage.xml \
    --junitxml=test_reports/backend_junit_report.xml

# remove venv
deactivate
rm -rf venv
