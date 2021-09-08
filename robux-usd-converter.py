#!/usr/bin/env python3
value = int(input('Number:'))
currency = input('(R)obux or (U)SD: ')
if currency.upper() == "R":
    final_result = value * 0.0125
    print(f"{final_result} USD")
else:
    final_result = value / 0.0125
    print(f"{final_result} Robux")
