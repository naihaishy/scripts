#!/bin/bash
sudo apt-get install python3-pip
pip install --upgrade pip
pip3 install -U -i https://mirrors.aliyun.com/pypi/simple/ aliyun-python-sdk-domain
python3 ali_dns_update.py
