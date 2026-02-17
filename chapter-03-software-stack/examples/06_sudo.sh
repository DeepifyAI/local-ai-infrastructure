#!/bin/bash
# Go to: https://www.nvidia.com/download/index.aspx
# Download the .run file for your GPU

# Remove any existing drivers
sudo apt purge nvidia-* -y
sudo apt autoremove -y

# Install dependencies
sudo apt install -y gcc make

# Stop display manager
sudo systemctl isolate multi-user.target

# Run installer
sudo bash NVIDIA-Linux-x86_64-550.54.14.run

# Follow prompts, accept defaults

# Start display manager
sudo systemctl start gdm3

# Reboot
sudo reboot
