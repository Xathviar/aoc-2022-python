solution = 0
helper = []
with open("input") as f:
    for line in f:
        line = line.strip()
        for c in line:
            if len(helper) == 14:
                if len(set(helper)) != 14:
                    del helper[0]
                else:
                    break
            solution += 1
            helper.append(c)
print(solution)
