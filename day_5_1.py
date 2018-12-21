with open('input.txt') as file:
    lines = file.read().splitlines()
    print("{}".format(len(lines)))
    line = lines[0]

    changes = True
    while changes is True:
        temp = ''
        i = 0
        limit = len(line)
        prev = limit
        print("{}".format(limit))
        while i < limit:
            if i + 1 >= limit:
                temp += line[i]
                break
            c1 = ord(line[i])
            c2 = ord(line[i+1])
            if abs(c1-32) == c2 or c1+32 == c2:
                #print("Dissolving {} and {}".format(line[i], line[i+1]))
                i += 2
            else:
                temp += line[i]
                i += 1
        line = temp
        if prev == len(line):
            changes = False
    print("{}".format(len(line)))
