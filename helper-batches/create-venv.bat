@echo off
cmd /k "pip install pip-tools & cd .. & python3 -m venv venv & pip-sync & .\env\Scripts\activate"