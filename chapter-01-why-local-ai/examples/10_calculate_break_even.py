#!/usr/bin/env python3
# cost_calculator.py

def calculate_break_even():
    """Interactive calculator for cloud vs local costs."""
    
    print("=== Local AI Cost Calculator ===\n")
    
    # Get user inputs
    daily_queries = int(input("Average queries per day: "))
    avg_tokens_input = int(input("Average input tokens per query: "))
    avg_tokens_output = int(input("Average output tokens per query: "))
    
    # Cloud pricing (OpenAI GPT-4o, Feb 2026)
    cloud_price_in = 0.005  # per 1K tokens
    cloud_price_out = 0.015
    
    # Calculate monthly cloud cost
    monthly_queries = daily_queries * 30
    monthly_tokens_in = monthly_queries * avg_tokens_input
    monthly_tokens_out = monthly_queries * avg_tokens_output
    
    cloud_monthly = (
        (monthly_tokens_in / 1000 * cloud_price_in) +
        (monthly_tokens_out / 1000 * cloud_price_out)
    )
    
    print(f"\n--- Cloud Costs ---")
    print(f"Monthly: ${cloud_monthly:.2f}")
    print(f"Annual:  ${cloud_monthly * 12:.2f}")
    
    # Local hardware options
    hardware_options = {
        'RTX 4090 Build': {'cost': 3500, 'power_w': 450},
        'Mac Studio M4 Ultra': {'cost': 4500, 'power_w': 200},
        'AI Workstation': {'cost': 4000, 'power_w': 250}
    }
    
    electricity_rate = 0.25  # $/kWh
    
    print(f"\n--- Local Hardware Break-Even ---")
    
    for name, specs in hardware_options.items():
        monthly_elec = (specs['power_w'] * 24 * 30) / 1000 * electricity_rate
        net_monthly_savings = cloud_monthly - monthly_elec
        
        if net_monthly_savings > 0:
            break_even_months = specs['cost'] / net_monthly_savings
            print(f"{name}:")
            print(f"  Hardware: ${specs['cost']}")
            print(f"  Monthly power: ${monthly_elec:.2f}")
            print(f"  Break-even: {break_even_months:.1f} months")
            print(f"  5-year savings: ${(net_monthly_savings * 60 - specs['cost']):.0f}")
        else:
            print(f"{name}: Cloud is cheaper at your usage level")
        
        print()

if __name__ == '__main__':
    calculate_break_even()
