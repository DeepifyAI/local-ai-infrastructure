#!/bin/bash
# Add NVIDIA container toolkit repo
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

# Install
sudo apt update
sudo apt install -y nvidia-container-toolkit

# Configure Docker to use it
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker

# Test GPU access from container
docker run --rm --gpus all nvidia/cuda:12.4.0-base-ubuntu22.04 nvidia-smi

# If you see nvidia-smi output, GPU passthrough works!
