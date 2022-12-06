solution = 0
helper = []
with open("input") as f:
    for line in f:
        line = line.strip()
        for c in line:
            if len(helper) == 4:
                if len(set(helper)) != 4:
                    del helper[0]
                else:
                    break
            solution += 1
            helper.append(c)
print(solution)
