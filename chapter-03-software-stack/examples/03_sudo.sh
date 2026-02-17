#!/bin/bash
# Update everything
sudo apt update && sudo apt upgrade -y

# Install essentials
sudo apt install -y \
    build-essential \
    curl \
    wget \
    git \
    vim \
    htop \
    net-tools \
    python3-pip \
    python3-venv

# Reboot
sudo reboot
