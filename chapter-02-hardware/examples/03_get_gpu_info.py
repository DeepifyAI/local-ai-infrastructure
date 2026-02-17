#!/usr/bin/env python3
# detect_hardware.py
"""
Detect AI-relevant hardware specs.
"""

import platform
import subprocess
import json

def get_gpu_info():
    """Detect GPU using nvidia-smi."""
    try:
        result = subprocess.run(
            ['nvidia-smi', '--query-gpu=name,memory.total', '--format=csv,noheader'],
            capture_output=True,
            text=True,
            check=True
        )
        
        gpus = []
        for line in result.stdout.strip().split('\n'):
            name, memory = line.split(',')
            gpus.append({
                'name': name.strip(),
                'vram_mb': int(memory.strip().split()[0])
            })
        
        return gpus
    
    except (FileNotFoundError, subprocess.CalledProcessError):
        # Try Apple Silicon
        if platform.system() == 'Darwin' and platform.machine() == 'arm64':
            return [{'name': 'Apple Silicon', 'vram_mb': 'Unified Memory'}]
        
        return []

def get_cpu_info():
    """Get CPU information."""
    return {
        'architecture': platform.machine(),
        'processor': platform.processor(),
        'system': platform.system()
    }

def get_memory_info():
    """Get RAM information."""
    try:
        if platform.system() == 'Linux':
            with open('/proc/meminfo', 'r') as f:
                for line in f:
                    if line.startswith('MemTotal'):
                        kb = int(line.split()[1])
                        return {'total_gb': round(kb / 1024 / 1024, 1)}
        
        elif platform.system() == 'Darwin':
            result = subprocess.run(
                ['sysctl', 'hw.memsize'],
                capture_output=True,
                text=True
            )
            bytes_mem = int(result.stdout.split()[1])
            return {'total_gb': round(bytes_mem / 1024**3, 1)}
    
    except:
        pass
    
    return {'total_gb': 'Unknown'}

def detect_all():
    """Full hardware detection."""
    return {
        'cpu': get_cpu_info(),
        'memory': get_memory_info(),
        'gpus': get_gpu_info()
    }

if __name__ == '__main__':
    info = detect_all()
    
    print("=== Hardware Detection ===\n")
    print(f"Architecture: {info['cpu']['architecture']}")
    print(f"System:       {info['cpu']['system']}")
    print(f"RAM:          {info['memory']['total_gb']} GB")
    
    if info['gpus']:
        print(f"\nGPUs:")
        for i, gpu in enumerate(info['gpus']):
            if isinstance(gpu['vram_mb'], int):
                vram_gb = gpu['vram_mb'] / 1024
                print(f"  [{i}] {gpu['name']} ({vram_gb:.1f} GB VRAM)")
            else:
                print(f"  [{i}] {gpu['name']} ({gpu['vram_mb']})")
    else:
        print("\nGPUs: None detected")
    
    # Save to JSON
    with open('hardware_info.json', 'w') as f:
        json.dump(info, f, indent=2)
    
    print("\nSaved to hardware_info.json")
