#!/usr/bin/env python3
# cost_calculator.py

# Cloud costs (OpenAI GPT-4o as of Feb 2026)
CLOUD_PRICE_INPUT = 0.005   # $ per 1K tokens
CLOUD_PRICE_OUTPUT = 0.015  # $ per 1K tokens

# Our actual usage (measured over 30 days)
daily_queries = 1200
avg_input_tokens = 800
avg_output_tokens = 300

# Monthly cloud cost
monthly_input_tokens = daily_queries * avg_input_tokens * 30
monthly_output_tokens = daily_queries * avg_output_tokens * 30

cloud_cost_monthly = (
    (monthly_input_tokens / 1000 * CLOUD_PRICE_INPUT) +
    (monthly_output_tokens / 1000 * CLOUD_PRICE_OUTPUT)
)

print(f"Monthly cloud cost: ${cloud_cost_monthly:.2f}")
print(f"Annual cloud cost: ${cloud_cost_monthly * 12:.2f}")

# Local costs
DGX_SPARK_PRICE = 18000  # one-time
POWER_CONSUMPTION = 250  # watts (measured)
ELECTRICITY_RATE = 0.25  # $/kWh (UK average)

monthly_electricity = (POWER_CONSUMPTION * 24 * 30) / 1000 * ELECTRICITY_RATE

print(f"\nLocal (DGX Spark):")
print(f"Hardware: ${DGX_SPARK_PRICE} (one-time)")
print(f"Monthly electricity: ${monthly_electricity:.2f}")

# Break-even calculation
break_even_months = DGX_SPARK_PRICE / (cloud_cost_monthly - monthly_electricity)
print(f"\nBreak-even: {break_even_months:.1f} months")
