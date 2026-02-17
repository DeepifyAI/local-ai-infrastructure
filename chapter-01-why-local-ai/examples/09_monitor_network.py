#!/usr/bin/env python3
# privacy_audit.py
import subprocess
import time
from ollama import chat

def monitor_network(duration=10):
    """Monitor network traffic during AI inference."""
    print(f"Monitoring network for {duration} seconds...")
    print("Running tcpdump (requires sudo)...\n")
    
    # Start network capture
    proc = subprocess.Popen(
        ['sudo', 'tcpdump', '-i', 'any', '-n', 'port', '443', '-c', '100'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    time.sleep(2)  # Let tcpdump start
    
    # Run inference
    print("Sending prompt to local model...")
    response = chat(
        model='gemma2:2b',
        messages=[{
            'role': 'user',
            'content': 'Write a short poem about privacy.'
        }]
    )
    
    print(f"\nResponse: {response['message']['content']}\n")
    
    # Wait for capture
    time.sleep(duration)
    proc.terminate()
    
    stdout, stderr = proc.communicate()
    packets = stdout.decode().count('\n')
    
    print(f"HTTPS packets captured: {packets}")
    print("Expected: 0 (if Ollama is running locally)")
    
    if packets == 0:
        print("✓ Privacy confirmed: No external network traffic!")
    else:
        print("⚠ Warning: Detected external traffic. Check your setup.")

if __name__ == '__main__':
    monitor_network()
