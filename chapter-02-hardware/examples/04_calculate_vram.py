#!/usr/bin/env python3
# vram_calculator.py
"""
Calculate VRAM requirements for models.
"""

def calculate_vram(params_billions, precision='4bit'):
    """
    Calculate VRAM requirement.
    
    Args:
        params_billions: Model size (e.g., 7 for 7B, 70 for 70B)
        precision: '4bit', '8bit', 'fp16', 'fp32'
    
    Returns:
        Required VRAM in GB (with 20% overhead)
    """
    
    bytes_per_param = {
        '4bit': 0.5,
        '8bit': 1.0,
        'fp16': 2.0,
        'fp32': 4.0
    }
    
    if precision not in bytes_per_param:
        raise ValueError(f"Unknown precision: {precision}")
    
    # Base calculation
    base_gb = params_billions * bytes_per_param[precision]
    
    # Add 20% overhead for KV cache, activations
    total_gb = base_gb * 1.2
    
    return total_gb

def what_fits(vram_gb):
    """Show what models fit in given VRAM."""
    
    models = [
        ('Gemma 2B', 2, 'Consumer laptop GPU'),
        ('Phi-3 Mini', 3.8, 'Fast, efficient'),
        ('Llama 3 8B', 8, 'Best quality for size'),
        ('Gemma 2 9B', 9, 'Good instruction following'),
        ('Mistral 7B', 7, 'Excellent reasoning'),
        ('Qwen 2.5 14B', 14, 'Multilingual'),
        ('Llama 3.1 70B', 70, 'Near-frontier quality'),
        ('Llama 3.1 405B', 405, 'Frontier-level')
    ]
    
    print(f"\n=== Models that fit in {vram_gb}GB VRAM ===\n")
    
    for precision in ['4bit', '8bit', 'fp16']:
        print(f"{precision.upper()}:")
        fits = False
        
        for name, size, note in models:
            required = calculate_vram(size, precision)
            if required <= vram_gb:
                print(f"  ✓ {name:<20} ({required:.1f}GB) - {note}")
                fits = True
        
        if not fits:
            print(f"  ✗ No models fit at {precision}")
        
        print()

if __name__ == '__main__':
    # Example: RTX 4090
    print("=== RTX 4090 (24GB VRAM) ===")
    what_fits(24)
    
    # Example: Mac Studio M4 Ultra
    print("\n=== Mac Studio M4 Ultra (192GB Unified) ===")
    what_fits(192)
