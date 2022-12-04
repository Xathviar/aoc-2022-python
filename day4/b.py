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
        numbers1 = []
        numbers2 = []
        for i in range(lowValue1, highValue1 + 1):
            numbers1.append(i)
        for i in range(lowValue2, highValue2 + 1):
            numbers2.append(i)
        if len(set(numbers1).intersection(numbers2)) > 0:
            # print(f"{line}: {numbers1} - {numbers2}")
            solution += 1
print(solution)
