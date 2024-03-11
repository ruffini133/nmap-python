#!/bin/bash
apt-get update
apt-get install -y nmap
pip install -r requirements.txt
python app.py
