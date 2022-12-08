from treelib import Node, Tree

solution = 0
currentWorkingDirectory = ""
tree = Tree()

with open("input") as f:
    for line in f:
        args = line.strip().split(" ")
        if args[0] == "$":
            command = args[1]
            if command == "cd":
                directory = args[2]
                if directory == "/":
                    currentWorkingDirectory = "/"
                    tree.create_node("/", "/", data=0)
                elif directory == "..":
                    currentWorkingDirectory = "/".join(currentWorkingDirectory.split("/")[0:-2]) + "/"
                else:
                    currentWorkingDirectory = f"{currentWorkingDirectory}{directory}/"
        elif args[0] == "dir":
            if currentWorkingDirectory == "/":
                tree.create_node(args[1], args[1], currentWorkingDirectory, data=0)
            else:
                try:
                    tree.create_node(args[1], args[1], currentWorkingDirectory.split("/")[-2], data=0)
                except:
                    continue
        else:
            value = int(args[0])
            filename = args[1]
            try:
                if currentWorkingDirectory == "/":
                    tree.create_node(filename, filename, currentWorkingDirectory, data=value)
                else:
                    tree.create_node(filename, filename, currentWorkingDirectory.split("/")[-2], data=value)
            except:
                continue


def solvetree(element):
    global solution
    foldersize = 0
    for node in tree.children(element.identifier):
        if node.data != 0:
            foldersize += node.data
        else:
            foldersize += solvetree(node)
    print(f"{element}: {foldersize}")
    if foldersize <= 100000:
        solution += foldersize
    return foldersize

helperData = 0
for node in tree.all_nodes_itr():
    helperData += node.data

solvetree(tree.get_node(tree.root))

# print(solution)
print(f"Sum of all Values: {helperData}")
