solution = 0
with open("input") as f:
    for line in f:
        opponent = ord(line[0]) - 64
        yourChoice = ord(line[2]) - 87
        solution += (yourChoice - 1) * 3
        if yourChoice == 2:
            solution += opponent
        if yourChoice == 1:
            if opponent == 1:
                solution += 3
            else:
                solution += opponent - 1
        if yourChoice == 3:
            if opponent == 3:
                solution += 1
            else:
                solution += opponent + 1
print(solution)
