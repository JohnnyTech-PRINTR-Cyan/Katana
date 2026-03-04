#!/bin/bash
# Katana Auto-Installer for macOS

# Colors
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${CYAN}════════════════════════════════════════════════════════════${NC}"
echo -e "  ${GREEN}⚔  Katana macOS Auto-Installer  ⚔${NC}"
echo -e "${CYAN}════════════════════════════════════════════════════════════${NC}"

# Check for Homebrew
if ! command -v brew &> /dev/null; then
    echo -e "▸ Homebrew not found. Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    
    # Add brew to PATH for the current session (standard Intel/Apple Silicon paths)
    if [ -d "/opt/homebrew/bin" ]; then
        eval "$(/opt/homebrew/bin/brew shellenv)"
    elif [ -d "/usr/local/bin" ]; then
         eval "$(/usr/local/bin/brew shellenv)"
    fi
else
    echo -e "▸ Homebrew is already installed."
fi

# Install Dependencies
echo -e "▸ Ensuring dependencies are installed via Homebrew..."
brew install python git curl

# Download install.py
echo -e "▸ Downloading Katana installer..."
INSTALLER_URL="https://raw.githubusercontent.com/jhi2/Katana/main/install.py"
curl -LO $INSTALLER_URL

# Execute installer
if [ -f "install.py" ]; then
    echo -e "▸ Launching Katana installer..."
    python3 install.py
else
    echo -e "${RED}✗ Failed to download install.py${NC}"
    exit 1
fi
