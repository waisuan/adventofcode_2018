import string

letters = list(string.ascii_lowercase)
#print(letters)

with open('input.txt') as file:
    lines = file.read().splitlines()
    print("{}".format(len(lines)))
    shortest = 999999

    for letter in letters:
        print("{}".format(letter))
        changes = True
        line = ''

        for l in lines[0]:
            if l.lower() == letter:
                continue
            line += l

        while changes is True:
            temp = ''
            i = 0
            limit = len(line)
            prev = limit
            while i < limit:
                if i + 1 >= limit:
                    temp += line[i]
                    break
                c1 = ord(line[i])
                c2 = ord(line[i+1])
                if abs(c1-32) == c2 or c1+32 == c2:
                    i += 2
                else:
                    temp += line[i]
                    i += 1
            line = temp
            if prev == len(line):
                changes = False
        print("{}".format(len(line)))
        if len(line) < shortest:
            shortest = len(line)
    print("{}".format(shortest))
