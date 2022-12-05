import re

solution = ""
configuration = {
    '1': ['S', 'C', 'V', 'N'],
    '2': ['Z', 'M', 'J', 'H', 'N', 'S'],
    '3': ['M', 'C', 'T', 'G', 'J', 'N', 'D'],
    '4': ['T', 'D', 'F', 'J', 'W', 'R', 'M'],
    '5': ['P', 'F', 'H'],
    '6': ['C', 'T', 'Z', 'H', 'J'],
    '7': ['D', 'P', 'R', 'Q', 'F', 'S', 'L', 'Z'],
    '8': ['C', 'S', 'L', 'H', 'D', 'F', 'P', 'W'],
    '9': ['D', 'S', 'M', 'P', 'F', 'N', 'G', 'Z'],
}

with open("input") as f:
    for line in f:
        line = line.strip()
        arguments = line.split(" ")
        amount = int(arguments[1])
        fromLocation = arguments[3]
        toLocation = arguments[5]
        firstPos = len(configuration[fromLocation]) - amount
        toAppend = configuration[fromLocation][firstPos:]
        configuration[toLocation].extend(toAppend)
        print("###############################################")
        print(line)
        print(firstPos)
        print(len(configuration[fromLocation]))
        print(len(configuration[toLocation]))
        print(configuration)
        print(toAppend)
        print("###############################################")
        del configuration[fromLocation][firstPos:]

for i in configuration:
    print(configuration[i][-1], end="")
