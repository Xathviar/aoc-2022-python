#!/usr/bin/env python
index = 0
highest_value = 0
counter = 0
value = 0
with open("input") as f:
    for line in f:
        if line.strip() == "":
            if value > highest_value:
                index = counter
                highest_value = value
            counter = counter + 1
            value = 0
        else:
            value += int(line)
print(f"{index} : {highest_value}")
