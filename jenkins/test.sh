#!/bin/bash

echo "Test Stage"

# install
sudo pip install pytest pytest-cov

# testing
python3 -m pytest \
    --cov=application \
    --cov-report term-missing \
    --cov-report xml:coverage.xml \
    --junitxml=junit_report.xml
