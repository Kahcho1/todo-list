#!/bin/bash

echo "Test Stage"

# create environment
python3 -m venv venv
source venv/bin/activate

# install
sudo pip install pytest pytest-cov

# testing
python3 -m pytest \
    --cov=application \
    --cov-report term-missing \
    --cov-report xml:coverage.xml \
    --junitxml=junit_report.xml

# quit
deactivate