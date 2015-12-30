#!/usr/bin/env bash
apt-get update
apt-get -y install build-essential
apt-get -y install python-dev

wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
pip install psutil
pip install pyyaml