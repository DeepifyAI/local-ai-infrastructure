#!/bin/bash
# Disconnect from the internet (Linux/Mac)
sudo ifconfig wlan0 down  # or your network interface

# Now go back to Ollama and ask another question
>>> What's 2+2?
