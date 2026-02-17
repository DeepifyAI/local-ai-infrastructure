#!/bin/bash
# Find your USB drive
lsblk

# Write image (CAREFUL: this erases the USB)
sudo dd if=ubuntu-22.04.4-desktop-amd64.iso of=/dev/sdX bs=4M status=progress
sudo sync
