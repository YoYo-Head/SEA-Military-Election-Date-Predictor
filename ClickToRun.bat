@echo off
setlocal

REM Get the directory where this bat file is located
set "BASE_DIR=%~dp0"

REM Remove trailing backslash
set "BASE_DIR=%BASE_DIR:~0,-1%"

REM Set paths dynamically
set "PYTHON=%BASE_DIR%\program\.venv\Scripts\python.exe"
set "SCRIPT=%BASE_DIR%\program\SMED.py"

REM Run the program
"%PYTHON%" "%SCRIPT%"

pause