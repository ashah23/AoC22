from treelib import Node, Tree
import sys

class FileNode(object):
    def __init__(self, name, path, filesize):
        self.name = name
        self.path = path
        self.filesize = filesize

def create_file_tree(filename):
    tree = Tree()
    dirs = set()
    tree.create_node("/", "", data=0)
    cur_node = tree.get_node("")
    with open(filename) as f:
        for line in f:
            cur_path = cur_node.__getattribute__("_identifier")
            args = line.strip().split(' ')
            arg0 = args[0]
            ## case when the line is a command
            if arg0 == "$":
                ## cd command
                if args[1] == "cd":
                    dir = args[2]
                    ## changing to parent dir
                    if dir == "..":
                        ## set cur_node to parent of cur_node
                        cur_node = tree.parent(cur_path)
                    elif not dir == "/":
                        ## set cur_node to a child node
                        cur_node = tree.get_node(cur_path + "/" + dir)
            ## case of a directory being listed
            elif arg0 == "dir":
                arg1 = args[1]
                tree.create_node(arg1, cur_path + "/" + arg1, parent=cur_node, data=0)
            ## case of a file
            else:
                ## file size is arg0
                filesize = int(arg0)
                name = args[1]
                tree.create_node(name, cur_path + "/" + name, parent=cur_node, data=filesize)
    return tree


filename = "Day7\\input.txt"
tree = create_file_tree(filename)
sizes = dict()

for nid in tree.expand_tree(mode=Tree.DEPTH):
    node = tree.get_node(nid)
    parent_dir = tree.parent(nid)

    if parent_dir is not None:
        name = parent_dir.__getattribute__("_identifier")
        size = node.__getattribute__("data")
        if sizes.__contains__(name):
            sizes[name] += size
        else:
            sizes[name] = size

for nid in tree.expand_tree(mode=Tree.DEPTH):
    if sizes.__contains__(nid):
        for key in sizes.keys():
            if not key == nid and key.startswith(nid):
                sizes[nid] += sizes[key]

## part 1
# sum = 0
# threshold = 100000

# for key in sizes.keys():
#     size = sizes[key]
#     if size <= threshold:
#         sum += size

# print("Sum: " + str(sum))

## part 2
smallest_dir = sys.maxsize
path = ""
total_space = 70000000
total_needed = 30000000
total_used = sizes[""]

needed_space = total_needed - (total_space - total_used)

print(str(needed_space))

for key in sizes.keys():
    size = sizes[key]
    if size > needed_space and size <= smallest_dir:
        smallest_dir = size
        path = key
        print("Path: " + path)
        print("Size: " + str(smallest_dir)) 

print("Path: " + path)
print("Size: " + str(smallest_dir))
