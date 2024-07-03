@echo off

rem
python --version | findstr /C:"Python 3.11.4" >nul
if %errorlevel% neq 0 (
    echo Installing Python 3.11.4...

    rem
    if not exist %SystemRoot%\System32\choco.exe (
        echo Installing Chocolatey...
        @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"
    )

    rem
    choco install python --version=3.11.4 -y
) else (
    echo Python 3.11.4 is already installed.
)

rem
pip install flask
pip install random

echo Installation complete.