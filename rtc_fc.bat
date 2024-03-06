@echo off
echo Service Started. . . .
rem cd C:\rtc-fc -- change this directory depending on where you are going to deploy it
rem call .\venv\Scripts\activate -- for development purposes
rem call python app.py
call waitress-serve --host 0.0.0.0 --port 5001 app:app