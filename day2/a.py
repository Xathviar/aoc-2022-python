solution = 0
with open("input") as f:
    for line in f:
        opponent = ord(line[0]) - 64
        yourChoice = ord(line[2]) - 87
        solution += yourChoice
        if opponent == yourChoice:
            solution += 3
        if yourChoice - 1 == opponent or (yourChoice == 1 and opponent == 3):
            solution += 6

print(solution)
