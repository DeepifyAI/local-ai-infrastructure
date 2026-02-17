#!/bin/bash
# setup_ai_stack.sh
# One-shot installation for Ubuntu 22.04 + NVIDIA GPU

set -e  # Exit on error

echo "=== AI Stack Installation ==="
echo "This script will install:"
echo "  - NVIDIA drivers"
echo "  - CUDA toolkit"
echo "  - Docker + NVIDIA container toolkit"
echo "  - Ollama"
echo ""
read -p "Continue? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    exit 1
fi

# Update system
echo ">>> Updating system..."
sudo apt update && sudo apt upgrade -y

# Install essentials
echo ">>> Installing essentials..."
sudo apt install -y \
    build-essential curl wget git vim htop \
    net-tools python3-pip python3-venv

# Install NVIDIA drivers
echo ">>> Installing NVIDIA drivers..."
sudo ubuntu-drivers autoinstall

# Install CUDA
echo ">>> Installing CUDA toolkit..."
wget -q https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.1-1_all.deb
sudo dpkg -i cuda-keyring_1.1-1_all.deb
sudo apt update
sudo apt install -y cuda-toolkit-12-4

# Add CUDA to PATH
if ! grep -q "cuda" ~/.bashrc; then
    echo 'export PATH=/usr/local/cuda/bin:$PATH' >> ~/.bashrc
    echo 'export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc
fi

# Install Docker
echo ">>> Installing Docker..."
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER

# Install NVIDIA Container Toolkit
echo ">>> Installing NVIDIA Container Toolkit..."
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
sudo apt update
sudo apt install -y nvidia-container-toolkit
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker

# Install Ollama
echo ">>> Installing Ollama..."
curl -fsSL https://ollama.com/install.sh | sh

echo ""
echo "=== Installation Complete ==="
echo ""
echo "IMPORTANT: Reboot your system now:"
echo "  sudo reboot"
echo ""
echo "After reboot, verify installation:"
echo "  nvidia-smi"
echo "  docker run --rm --gpus all nvidia/cuda:12.4.0-base-ubuntu22.04 nvidia-smi"
echo "  ollama --version"
echo ""
echo "Then pull your first model:"
echo "  ollama pull gemma2:2b"
echo ""
