#!/usr/bin/env python3
# Consumer GPU build
RTX_4090_BUILD = 3500  # GPU + PC
POWER_CONSUMPTION = 450  # watts (under load)

monthly_electricity = (450 * 24 * 30) / 1000 * 0.25  # $81

break_even = 3500 / (1890 - 81)
print(f"RTX 4090 build break-even: {break_even:.1f} months")
# Output: 1.9 months
