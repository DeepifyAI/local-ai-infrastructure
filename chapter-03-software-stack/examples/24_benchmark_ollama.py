#!/usr/bin/env python3
# multi_runtime_benchmark.py
"""
Compare inference speed across runtimes.
"""

import time
import subprocess
from ollama import chat

def benchmark_ollama(model, prompt, runs=5):
    """Benchmark Ollama."""
    latencies = []
    
    for _ in range(runs):
        start = time.time()
        chat(model=model, messages=[{'role': 'user', 'content': prompt}])
        latencies.append(time.time() - start)
    
    return {
        'runtime': 'Ollama',
        'model': model,
        'avg_latency': sum(latencies) / len(latencies)
    }

def benchmark_llamacpp(model_path, prompt, runs=5):
    """Benchmark llama.cpp."""
    latencies = []
    
    for _ in range(runs):
        start = time.time()
        subprocess.run(
            ['./llama.cpp/main', '-m', model_path, '-p', prompt, '-n', '50'],
            capture_output=True,
            check=True
        )
        latencies.append(time.time() - start)
    
    return {
        'runtime': 'llama.cpp',
        'model': model_path,
        'avg_latency': sum(latencies) / len(latencies)
    }

if __name__ == '__main__':
    prompt = "Explain quantum computing in one sentence."
    
    results = []
    
    # Test Ollama
    print("Testing Ollama...")
    results.append(benchmark_ollama('gemma2:2b', prompt))
    
    # Test llama.cpp (if available)
    # results.append(benchmark_llamacpp('models/gemma-2b-q4.gguf', prompt))
    
    print("\n=== Benchmark Results ===\n")
    for r in results:
        print(f"{r['runtime']:15} {r['model']:30} {r['avg_latency']*1000:.0f}ms")
