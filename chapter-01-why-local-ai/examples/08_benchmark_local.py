#!/usr/bin/env python3
# latency_benchmark.py
import time
import statistics
from ollama import chat

def benchmark_local(model, prompt, runs=10):
    """Benchmark local Ollama inference."""
    latencies = []
    
    for _ in range(runs):
        start = time.time()
        chat(model=model, messages=[{'role': 'user', 'content': prompt}])
        latency = (time.time() - start) * 1000  # convert to ms
        latencies.append(latency)
    
    return {
        'min': min(latencies),
        'max': max(latencies),
        'mean': statistics.mean(latencies),
        'median': statistics.median(latencies),
        'p95': sorted(latencies)[int(len(latencies) * 0.95)]
    }

# Test with a simple prompt
prompt = "Say hello in one word."

print("Benchmarking local inference (Gemma2 9B)...")
results = benchmark_local('gemma2:9b', prompt, runs=5)

print(f"\nLatency Statistics (ms):")
print(f"  Min:    {results['min']:.1f}")
print(f"  Median: {results['median']:.1f}")
print(f"  Mean:   {results['mean']:.1f}")
print(f"  P95:    {results['p95']:.1f}")
print(f"  Max:    {results['max']:.1f}")
