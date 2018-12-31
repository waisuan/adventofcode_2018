class Node:
    def __init__(self, id, children, no_of_entries, parent):
        self.id = id
        self.children = int(children)
        self.next = 2
        self.no_of_entries = int(no_of_entries)
        self.entries = []
        self.progress = int(children)
        self.parent = parent

with open('input.txt') as file:
    lines = file.read().splitlines()
    line = lines[0].split()
    print(line)
    root = Node(0, line[0], line[1], -1)
    tree = []
    stack = [root]
    while len(stack) != 0:
        print("{} {} {}".format(stack[-1].id, line[stack[-1].id], stack[-1].progress))
        if stack[-1].progress != 0:
            parent = stack[-1]
            node = Node(parent.id + parent.next,
                        line[parent.id + parent.next], line[parent.id + parent.next + 1], parent.id)
            stack.append(node)
        else:
            node = stack.pop()
            for i in range(node.id + node.next, node.id + node.next + node.no_of_entries):
                node.entries.append(line[i])
            if node.parent != -1:
                stack[-1].next = stack[-1].next + (node.no_of_entries + 2)
                if node.next != 2:
                    stack[-1].next = stack[-1].next + node.next - 2
                stack[-1].progress = stack[-1].progress - 1
                print("--- {} {} --> {}".format(node.parent, stack[-1].next, stack[-1].progress))
            tree.append(node)
    result = 0
    for node in tree:
        print("{} --> {}".format(line[node.id], node.entries))
        result += sum(int(x) for x in node.entries)
    print("{}".format(result))

