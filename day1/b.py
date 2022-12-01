#!/usr/bin/env python
highest_value = 0
s_highest_value = 0
t_highest_value = 0
counter = 0
value = 0
with open("input") as f:
    for line in f:
        if line.strip() == "":
            if value > highest_value:
                s_highest_value = highest_value
                t_highest_value = s_highest_value
                highest_value = value
            elif value > s_highest_value:
                t_highest_value = s_highest_value
                s_highest_value = value
            elif value > t_highest_value:
                t_highest_value = value
            value = 0
        else:
            value += int(line)
print(f"{highest_value+s_highest_value+t_highest_value}")
