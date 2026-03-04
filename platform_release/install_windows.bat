@echo off
setlocal

echo ════════════════════════════════════════════════════════════
echo   ⚔  Katana Windows Auto-Installer  ⚔
echo ════════════════════════════════════════════════════════════

:: Check for Git
where git >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo ▸ Git not found. Attempting to install via winget...
    winget install --id Git.Git -e --source winget
) else (
    echo ▸ Git is already installed.
)

:: Check for Python
where python >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo ▸ Python not found. Attempting to install via winget...
    winget install --id Python.Python.3.12 -e --source winget
) else (
    echo ▸ Python is already installed.
)

:: Refresh environment variables (simple way for current session)
:: Note: Full path refresh usually requires a new shell, but we try common paths
set PATH=%PATH%;%USERPROFILE%\AppData\Local\Programs\Python\Python312\;%USERPROFILE%\AppData\Local\Programs\Python\Python312\Scripts\

:: Download install.py
echo ▸ Downloading Katana installer...
set INSTALLER_URL=https://raw.githubusercontent.com/jhi2/Katana/main/install.py

curl -LO %INSTALLER_URL%

:: Execute installer
if exist install.py (
    echo ▸ Launching Katana installer...
    python install.py
) else (
    echo ✗ Failed to download install.py. Please check your internet connection.
    pause
    exit /b 1
)

pause
