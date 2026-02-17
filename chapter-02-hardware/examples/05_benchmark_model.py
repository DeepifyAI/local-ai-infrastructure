#!/usr/bin/env python3
# benchmark.py
"""
Standard AI inference benchmark.
"""

import time
from ollama import chat

def benchmark_model(model, prompts, runs=5):
    """
    Benchmark a model across multiple prompts.
    
    Returns: {
        'model': str,
        'avg_latency_ms': float,
        'tokens_per_second': float,
        'ttft_ms': float  # time to first token
    }
    """
    
    latencies = []
    ttfts = []
    total_tokens = 0
    
    print(f"Benchmarking {model}...")
    
    for prompt in prompts:
        for _ in range(runs):
            start = time.time()
            first_token_time = None
            tokens = 0
            
            response = chat(
                model=model,
                messages=[{'role': 'user', 'content': prompt}],
                stream=True
            )
            
            for chunk in response:
                if first_token_time is None:
                    first_token_time = time.time()
                tokens += 1
            
            end = time.time()
            
            latencies.append((end - start) * 1000)
            if first_token_time:
                ttfts.append((first_token_time - start) * 1000)
            total_tokens += tokens
    
    total_time = sum(latencies) / 1000
    
    return {
        'model': model,
        'avg_latency_ms': sum(latencies) / len(latencies),
        'tokens_per_second': total_tokens / total_time,
        'ttft_ms': sum(ttfts) / len(ttfts) if ttfts else 0
    }

# Standard benchmark prompts
BENCHMARK_PROMPTS = [
    "Write a hello world program in Python.",
    "Explain quantum computing in one sentence.",
    "What's 15% of 240?",
    "Write a haiku about AI.",
]

if __name__ == '__main__':
    models = ['gemma2:9b']  # Add your models
    
    results = []
    
    for model in models:
        try:
            result = benchmark_model(model, BENCHMARK_PROMPTS[:2], runs=2)
            results.append(result)
        except Exception as e:
            print(f"Failed to benchmark {model}: {e}")
    
    # Print results
    print("\n=== Benchmark Results ===\n")
    print(f"{'Model':<20} {'Avg Latency':<15} {'Tokens/sec':<12} {'TTFT':<10}")
    print("-" * 60)
    
    for r in results:
        print(f"{r['model']:<20} {r['avg_latency_ms']:<15.0f}ms {r['tokens_per_second']:<12.1f} {r['ttft_ms']:<10.0f}ms")
