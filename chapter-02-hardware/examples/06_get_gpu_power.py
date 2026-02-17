#!/usr/bin/env python3
# power_monitor.py
"""
Monitor GPU power consumption.
"""

import subprocess
import time
import json
from datetime import datetime

def get_gpu_power():
    """Get current GPU power draw in watts."""
    try:
        result = subprocess.run(
            ['nvidia-smi', '--query-gpu=power.draw', '--format=csv,noheader,nounits'],
            capture_output=True,
            text=True,
            check=True
        )
        
        return float(result.stdout.strip())
    
    except:
        return None

def monitor_power(duration_seconds=60, interval=1):
    """
    Monitor power over time.
    
    Returns: {
        'readings': [(timestamp, watts)],
        'avg_watts': float,
        'kwh': float,
        'cost_usd': float (at $0.12/kWh)
    }
    """
    
    readings = []
    start = time.time()
    
    print(f"Monitoring power for {duration_seconds} seconds...")
    
    while time.time() - start < duration_seconds:
        watts = get_gpu_power()
        if watts:
            readings.append((datetime.now().isoformat(), watts))
            print(f"  {watts:.1f}W", end='\r')
        time.sleep(interval)
    
    print()
    
    if not readings:
        return None
    
    avg_watts = sum(w for _, w in readings) / len(readings)
    hours = duration_seconds / 3600
    kwh = (avg_watts * hours) / 1000
    cost = kwh * 0.12  # $0.12/kWh
    
    return {
        'readings': readings,
        'avg_watts': avg_watts,
        'kwh': kwh,
        'cost_usd': cost
    }

if __name__ == '__main__':
    # Monitor during inference
    print("Start your AI workload now...")
    time.sleep(5)
    
    results = monitor_power(duration_seconds=120)
    
    if results:
        print(f"\n=== Power Consumption ===")
        print(f"Average: {results['avg_watts']:.1f}W")
        print(f"Energy used: {results['kwh']*1000:.2f} Wh")
        print(f"Cost (2 min): ${results['cost_usd']:.4f}")
        
        # Project costs
        monthly_kwh = results['avg_watts'] * 24 * 30 / 1000
        monthly_cost = monthly_kwh * 0.12
        
        print(f"\nIf running 24/7:")
        print(f"  Monthly: {monthly_kwh:.1f} kWh = ${monthly_cost:.2f}")
        print(f"  Annual: {monthly_kwh*12:.1f} kWh = ${monthly_cost*12:.2f}")
        
        # Save data
        with open('power_log.json', 'w') as f:
            json.dump(results, f, indent=2)
        
        print("\nSaved to power_log.json")
