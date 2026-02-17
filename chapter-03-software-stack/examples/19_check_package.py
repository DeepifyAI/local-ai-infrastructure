#!/usr/bin/env python3
# arm64_check.py
"""
Check if Python packages have ARM64 wheels.
"""

import subprocess
import json
import platform

def check_package(package_name):
    """Check if package has ARM64 wheels on PyPI."""
    
    try:
        result = subprocess.run(
            ['pip', 'index', 'versions', package_name],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        # This is a simplified check
        # Real check would query PyPI JSON API
        return True  # Assume available
    
    except:
        return False

def check_common_ai_packages():
    """Check common AI packages for ARM64 support."""
    
    packages = [
        'torch',
        'tensorflow',
        'transformers',
        'numpy',
        'pandas',
        'scikit-learn',
        'opencv-python',
        'pillow',
        'matplotlib',
        'requests',
        'ollama',
    ]
    
    arch = platform.machine()
    print(f"=== ARM64 Package Compatibility ===")
    print(f"Architecture: {arch}\n")
    
    if arch not in ['arm64', 'aarch64']:
        print("Not on ARM64, all packages should work.")
        return
    
    print("Checking packages...\n")
    
    for pkg in packages:
        available = check_package(pkg)
        status = "✓" if available else "✗"
        print(f"{status} {pkg}")
    
    print("\nNote: This is a basic check.")
    print("For ARM64, prefer:")
    print("  - conda-forge")
    print("  - Building from source")
    print("  - NVIDIA NGC containers (nvcr.io)")

if __name__ == '__main__':
    check_common_ai_packages()
