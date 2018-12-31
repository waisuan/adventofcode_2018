class Node:
    def __init__(self, id, children_count, no_of_entries, parent):
        self.id = id
        self.children_count = int(children_count)
        self.next = 2
        self.no_of_entries = int(no_of_entries)
        self.entries = []
        self.progress = int(children_count)
        self.parent = parent
        self.has_children = False if self.children_count == 0 else True
        self.value = 0
        self.children = []

with open('input.txt') as file:
    lines = file.read().splitlines()
    line = lines[0].split()
    print(line)
    root = Node(0, line[0], line[1], -1)
    tree = []
    tracker = {}
    stack = [root]
    while len(stack) != 0:
        print("{} {} {}".format(stack[-1].id, line[stack[-1].id], stack[-1].progress))
        if stack[-1].progress != 0:
            parent = stack[-1]
            node = Node(parent.id + parent.next,
                        line[parent.id + parent.next], line[parent.id + parent.next + 1], parent.id)
            stack[-1].children.append(node.id)
            stack.append(node)
        else:
            node = stack.pop()
            for i in range(node.id + node.next, node.id + node.next + node.no_of_entries):
                node.entries.append(int(line[i]))
            if node.parent != -1:
                stack[-1].next = stack[-1].next + (node.no_of_entries + 2)
                if node.next != 2:
                    stack[-1].next = stack[-1].next + node.next - 2
                stack[-1].progress = stack[-1].progress - 1
                print("--- {} {} --> {}".format(node.parent, stack[-1].next, stack[-1].progress))
            if node.has_children is not True:
                node.value = sum(int(x) for x in node.entries)
            else:
                for e in node.entries:
                    if e != 0 and e <= node.children_count:
                        node.value += tracker[node.children[e-1]].value
                        #node.value += sum(tracker[x].value for x in node.children)
            tree.append(node)
            tracker[node.id] = node
    print("{}".format(tracker[0].value))