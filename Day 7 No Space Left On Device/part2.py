from anytree import AnyNode, RenderTree, PostOrderIter

def calc_size(node):
    print(node.id)
    if node.id == "root" : return
    int(node.size)
    node.parent.size += node.size

TOTAL_DISC_SPACE = 70000000
DISC_SPACE_FOR_UPDATE = 30000000

required_for_delete = 0
min_size = 0

def find_dir_to_delete(node):
    global required_for_delete
    global min_size
    if(node.type=="DIR" and node.size<min_size and node.size>required_for_delete): min_size = node.size


with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f]
    max_line_len = 0
    root = AnyNode(id="root", type="DIR", size=0)
    current = root
    for line in lines:
        print("======================================")
        print("current: ", current)
        print("line: ", line)
        if line[0] == "$":
            print("COMMAND")
            if line[2:4] == "cd":
                print("CHANGE DIRECTORY")
                if line == "$ cd /" :
                    print("ROOT")
                    current = root
                elif line == "$ cd .." :
                    print("OUT")
                    current = current.parent
                else :
                    print("IN")
                    dir_in = line.split(" ")[2]
                    print("dir_in: ", dir_in)
                    print("current.children: ",current.children)
                    for child in current.children:
                        print("child: ", child)
                        if child.id == dir_in:
                            current = child
                            break
            if line[2:4] == "ls":
                print("LIST")
        else:
            print("RESULT")
            if line[0:3] == "dir":
                print("DIRECTORY")
                name = line[4:]
                newNode = AnyNode(id=name, parent=current, type="DIR", size=0)
            else:
                print("FILE")
                size = int(line.split(" ")[0])
                name = line.split(" ")[1]
                print("size: ", size)
                print("name: ", name)
                newNode = AnyNode(id=name, parent=current, type="FILE", size=size)

    print(RenderTree(root))
    [calc_size(node) for node in PostOrderIter(root)]
    print(RenderTree(root))
    free_space = TOTAL_DISC_SPACE - root.size
    print("free_space: ", free_space)
    required_for_delete = DISC_SPACE_FOR_UPDATE - free_space
    print("required_for_delete: ", required_for_delete)
    min_size = root.size
    [find_dir_to_delete(node) for node in PostOrderIter(root)]
    print("min_size: ", min_size)
