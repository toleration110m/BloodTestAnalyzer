@echo off
echo Starting packages upgrade...

python.exe -m pip install --upgrade pip

python -m pip install --upgrade matplotlib
python -m pip install --upgrade reportlab
python -m pip install --upgrade openpyxl
python -m pip install --upgrade test

if %errorlevel% equ 0 (
    echo Successfully installed/upgraded packages!
) else (
    echo Failed to install/upgrade packages. Error code: %errorlevel%
)
echo.
echo Press any key to close...
pause > nul