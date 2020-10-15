#!/bin/bash

#if mac
pip3 install -r requirements.txt
pyinstaller -Fw -i=icons/icon.icns -n NBwar-setup --hidden-import requests app.py 
