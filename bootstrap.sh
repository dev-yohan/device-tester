#!/usr/bin/env bash
apt-get update
apt-get -y install build-essential
apt-get -y install python-dev
apt-get -y install tcl8.5

wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
pip install psutil
pip install pyyaml
pip install requests
pip install rq


wget http://download.redis.io/releases/redis-stable.tar.gz
tar xzf redis-stable.tar.gz
cd redis-stable
make
make test
make install
cd utils
bash install_server.sh
service redis_6379 start

