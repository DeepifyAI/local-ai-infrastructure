#!/bin/bash
# Launch driver manager
sudo ubuntu-drivers devices

# You'll see available drivers:
# nvidia-driver-535 (recommended)
# nvidia-driver-545
# nvidia-driver-550

# Install recommended driver
sudo ubuntu-drivers autoinstall

# Reboot
sudo reboot
