from treelib import Node, Tree
import traceback

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
                tree.create_node(f"{currentWorkingDirectory}{args[1]}/", f"{currentWorkingDirectory}{args[1]}/", currentWorkingDirectory, data=0)
            else:
                try:
                    tree.create_node(f"{currentWorkingDirectory}{args[1]}/", f"{currentWorkingDirectory}{args[1]}/", currentWorkingDirectory, data=0)
                except Exception as ex:
                    traceback.print_exception(type(ex), ex, ex.__traceback__)
                    continue
        else:
            value = int(args[0])
            filename = args[1]
            try:
                if currentWorkingDirectory == "/":
                    tree.create_node(f"{currentWorkingDirectory}{filename}", f"{currentWorkingDirectory}{filename}", currentWorkingDirectory, data=value)
                else:
                    tree.create_node(f"{currentWorkingDirectory}{filename}", f"{currentWorkingDirectory}{filename}", currentWorkingDirectory, data=value)
            except Exception as ex:
                traceback.print_exception(type(ex), ex, ex.__traceback__)
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


print(solution)
print(f"Sum of all Values: {helperData}")
