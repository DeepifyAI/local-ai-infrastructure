#!/usr/bin/env python3
"""Chapter 1: Why local? The cost breakdown."""

print("=== Cloud vs Local: Cost Comparison ===")
print()

# Real pricing (Feb 2026)
cloud_per_1k = 0.03  # GPT-4o per 1K tokens (output)
queries_per_day = 200
avg_tokens = 800
days = 365

cloud_annual = (queries_per_day * avg_tokens / 1000) * cloud_per_1k * days
print(f"Cloud (GPT-4o):")
print(f"  {queries_per_day} queries/day x {avg_tokens} tokens x ${cloud_per_1k}/1K tokens")
print(f"  Annual cost: ${cloud_annual:,.2f}")
print()

local_hw = 500  # decent GPU
local_power = 0.15 * 8 * 365  # 150W * 8hrs * 365 days at $0.12/kWh
local_power_cost = local_power * 0.12 / 1000
local_total = local_hw + local_power_cost
print(f"Local (your hardware):")
print(f"  Hardware (one-time): ${local_hw}")
print(f"  Power (annual):      ${local_power_cost:,.2f}")
print(f"  Year 1 total:        ${local_total:,.2f}")
print()

savings = cloud_annual - local_total
print(f"Year 1 savings: ${savings:,.2f}")
print(f"Year 2 savings: ${cloud_annual - local_power_cost:,.2f} (hardware already paid)")
print()
print(f"Break-even: {local_hw / (cloud_annual/365):.0f} days")
print()
print("Local wins. Every time.")
