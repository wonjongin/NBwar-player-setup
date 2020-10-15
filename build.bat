@echo off
@rem build for windows

pip install -r requirements.txt
pyinstaller -Fw -i=icons/icon.ico -n NBwar-setup app.py 