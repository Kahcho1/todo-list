#!/bin/bash

# install apt
sudo apt update
sudo apt install python3-venv python3-pip python3 -y

# create venv
python3 -m venv venv

# activate venv
source venv/bin/activate

# install pip requitments
pip3 install -r requirements.txt