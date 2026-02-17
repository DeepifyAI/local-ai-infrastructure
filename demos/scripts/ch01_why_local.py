#!/usr/bin/env python3
"""
Why local AI? Let the numbers answer.
"""

print("=== Why Run AI Locally? The Numbers. ===\n")

# -- Cloud costs (GPT-4o, Feb 2026 pricing) --
daily_queries   = 1000
tokens_per_query = 1000          # avg input + output
cloud_per_1k    = 0.010          # $ blended
monthly_cloud   = (daily_queries * tokens_per_query * 30) / 1000 * cloud_per_1k
annual_cloud    = monthly_cloud * 12

print(f"Usage assumption:  {daily_queries:,} queries/day  ·  {tokens_per_query:,} tokens each")
print()
print(f"☁  Cloud (GPT-4o):   ${monthly_cloud:>8,.0f}/month   →  ${annual_cloud:,.0f}/year")

# -- Local hardware --
hardware_cost = 3_500            # RTX 4090 build
monthly_power = 81               # $  (450W · 24h · 30d · $0.25/kWh)
monthly_saving = monthly_cloud - monthly_power
break_even_months = hardware_cost / monthly_saving
saving_5yr = monthly_saving * 60 - hardware_cost

print(f"🖥  Local (RTX 4090): ${hardware_cost:>8,} one-time  +  ${monthly_power}/month electricity")
print()
print(f"Break-even:    {break_even_months:.1f} months")
print(f"5-year saving: ${saving_5yr:,.0f}")
print()

# -- Privacy --
print("─" * 42)
print("Privacy: every query stays on-device.")
print("Latency: no network round-trip (sub-second).")
print("Control: you own the weights. No deprecations.")
