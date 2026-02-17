#!/bin/bash
# While running inference
sudo powermetrics --samplers gpu_power -i 1000 -n 1

# You should see GPU power usage increase
