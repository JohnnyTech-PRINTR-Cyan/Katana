#!/bin/bash
# Katana Auto-Installer for Linux

# Colors
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${CYAN}════════════════════════════════════════════════════════════${NC}"
echo -e "  ${GREEN}⚔  Katana Linux Auto-Installer  ⚔${NC}"
echo -e "${CYAN}════════════════════════════════════════════════════════════${NC}"

# Detect Package Manager
if [ -f /etc/debian_version ]; then
    PM="apt"
elif [ -f /etc/redhat-release ]; then
    PM="dnf"
elif [ -f /etc/arch-release ]; then
    PM="pacman"
elif [ -f /etc/os-release ]; then
    # Fallback to os-release
    . /etc/os-release
    case "$ID" in
        ubuntu|debian|pop|kali|linuxmint) PM="apt" ;;
        fedora|rhel|centos) PM="dnf" ;;
        arch|manjaro) PM="pacman" ;;
        suse|opensuse*) PM="zypper" ;;
        *) PM="unknown" ;;
    esac
else
    PM="unknown"
fi

echo -e "▸ Detected package manager: ${CYAN}$PM${NC}"

# Install Dependencies
install_deps() {
    echo -e "▸ Installing dependencies..."
    case "$PM" in
        apt)
            sudo apt update
            sudo apt install -y python3 python3-venv git curl wget
            ;;
        dnf)
            sudo dnf install -y python3 git curl wget
            ;;
        pacman)
            sudo pacman -Sy --noconfirm python git curl wget
            ;;
        zypper)
            sudo zypper install -y python3 git curl wget
            ;;
        *)
            echo -e "${RED}✗ Unsupported distribution. Please install python3, git, and curl manually.${NC}"
            exit 1
            ;;
    esac
}

# Check for existing tools
if ! command -v python3 &> /dev/null || ! command -v git &> /dev/null || ! command -v curl &> /dev/null; then
    install_deps
fi

# Download install.py
echo -e "▸ Downloading Katana installer..."
INSTALLER_URL="https://raw.githubusercontent.com/jhi2/Katana/main/install.py"

if command -v curl &> /dev/null; then
    curl -LO $INSTALLER_URL
elif command -v wget &> /dev/null; then
    wget $INSTALLER_URL
else
    echo -e "${RED}✗ Neither curl nor wget found. Cannot download installer.${NC}"
    exit 1
fi

# Execute installer
if [ -f "install.py" ]; then
    echo -e "▸ Launching Katana installer..."
    python3 install.py
else
    echo -e "${RED}✗ Failed to download install.py${NC}"
    exit 1
fi
