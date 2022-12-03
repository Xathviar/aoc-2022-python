solution = 0
hlparray = []
with open("input") as f:
    for line in f:
        line = line.strip()
        hlparray.append(line)
        if len(hlparray) == 3:
            for letter in line:
                if letter in hlparray[0] and letter in hlparray[1]:
                    if ord(letter) > 90:
                        print(f"{letter}: {ord(letter) - 96}")
                        solution += ord(letter) - 96
                    else:
                        print(f"{letter}: {ord(letter) - 38}")
                        solution += ord(letter) - 38
                    break
            hlparray = []
print(solution)
