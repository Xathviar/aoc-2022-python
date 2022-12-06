solution = 0
with open("input") as f:
    for line in f:
        line = line.strip()
        compartment1 = line[0:int(len(line) / 2)]
        compartment2 = line[int(len(line) / 2):]
        for letter in compartment1:
            if letter in compartment2:
                if ord(letter) > 90:
                    print(f"{letter}: {ord(letter) - 96}")
                    solution += ord(letter) - 96
                else:
                    print(f"{letter}: {ord(letter) - 38}")
                    solution += ord(letter) - 38
                break
print(solution)
