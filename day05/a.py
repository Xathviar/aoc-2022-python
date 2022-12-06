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


def moveFromTo(fromLocation, toLocation, configuration):
    configuration[toLocation].append(configuration[fromLocation][-1])
    del configuration[fromLocation][-1]


with open("input") as f:
    for line in f:
        line = line.strip()
        arguments = line.split(" ")
        amount = int(arguments[1])
        fromLocation = arguments[3]
        toLocation = arguments[5]
        print(line)
        for i in range(0, amount):
            print(f"Moving from {fromLocation} to {toLocation}")
            moveFromTo(fromLocation, toLocation, configuration)

for i in configuration:
    print(configuration[i][-1],end="")
