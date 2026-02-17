#!/bin/bash
# Start a local model
$ ollama run gemma2:9b

# Send a prompt
>>> Analyze this contract for unusual clauses: [paste 50-page NDA]

# Check network traffic
$ sudo tcpdump -i any port 443 -c 10

# Result: ZERO packets. Nothing left your network.
