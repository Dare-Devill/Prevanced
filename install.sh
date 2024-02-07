#!/data/data/com.termux/files/usr/bin/bash

# Update package lists
pkg update

# Upgrade installed packages
pkg upgrade

# Install Python and pip
pkg install python
pkg install clang
pkg install libffi
pip install --upgrade pip

# Install required Python libraries
pip install requests
pip install colorama
pip install pyfiglet

# Create a directory for the script
mkdir -p ~/bin
cd ~/bin

# Download the script and rename it
curl -o prevanced.py https://raw.githubusercontent.com/Dare-Devill/Prevanced/main/prevanced.py

# Make the script executable
chmod +x prevanced.py

# Create a symbolic link in a directory that's in the PATH
mkdir -p ~/.termux/tasker/
ln -s ~/bin/prevanced.py ~/.termux/tasker/prevanced

# Run the script
prevanced
