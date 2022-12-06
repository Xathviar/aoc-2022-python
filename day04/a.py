solution = 0
with open("input") as f:
    for line in f:
        line = line.strip()
        pair1 = line.split(',')[0]
        pair2 = line.split(',')[1]
        lowValue1 = int(pair1.split('-')[0])
        highValue1 = int(pair1.split('-')[1])
        lowValue2 = int(pair2.split('-')[0])
        highValue2 = int(pair2.split('-')[1])
        if lowValue1 <= lowValue2 and highValue1 >= highValue2:
            solution += 1
        elif lowValue2 <= lowValue1 and highValue2 >= highValue1:
            solution += 1

print(solution)